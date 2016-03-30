---
title: jni 通过c/c++返回HashMap等复杂参数给java
categories:
- 文章
tags: 
- jni
date: 2015-07-02 16:15:11
---

  返回其他对象与这个相似，可以自己研究下

思路：

    1.创建HashMap对象：
    /*C语言版本，下同*/
    //获取java的HashMap类
    jclass class_hashmap=(*env)->FindClass(env,"java/util/HashMap");
    //获取类似于java 的new HashMap();
    jmethodID hashmap_init=(*env)->GetMethodID(env,class_hashmap,"<init>","()V");
    //初始化。类似于hashMap=new HashMap();
    jobject HashMap=(*env)->NewObject(env,class_hashmap,hashmap_init,"");
    //获取hashMap.put()的ID
    jmethodID HashMap_put=(*env)->GetMethodID(env,class_hashmap,"put",
        "(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;");

<!-- more -->
   2\. 赋值：

    //类似于map.put("key","value");
        //(*env)->NewStringUTF(env, "key值")不能直接用"key值"替代
      (*env)->CallObjectMethod(env, HashMap, HashMap_put, (*env)->NewStringUTF(env, "key值"), (*env)->NewStringUTF(env, "value值"));

全部代码：

    JniClient.java
    package com.ndk.test;
    import java.util.HashMap;
    public class JniClient {
        public static native HashMap<String, String> setMap();
    }

JniClient.c

    #include "com_ndk_test_JniClient.h"
    #include<stdio.h>
    #ifdef __cplusplus
    extern "C"
    {
    #endif
    JNIEXPORT jobject JNICALL Java_com_ndk_test_JniClient_setMap(JNIEnv *env,
            jclass cls) {
        jclass class_hashmap = (*env)->FindClass(env, "java/util/HashMap");
        jmethodID hashmap_init = (*env)->GetMethodID(env, class_hashmap, "<init>",
                "()V");
        jobject HashMap = (*env)->NewObject(env, class_hashmap, hashmap_init, "");
        jmethodID HashMap_put = (*env)->GetMethodID(env, class_hashmap, "put",
                "(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;");
        (*env)->CallObjectMethod(env, HashMap, HashMap_put, (*env)->NewStringUTF(env, "key1"), (*env)->NewStringUTF(env, "value1"));
        (*env)->CallObjectMethod(env, HashMap, HashMap_put,(*env)->NewStringUTF(env, "key2"), (*env)->NewStringUTF(env, "value2"));
        return HashMap;
    }
    #ifdef __cplusplus
    }
    #endif

引用方法：

    Object object=JniClient.setMap();
    HashMap<String, String>map=(HashMap<String, String>)object;
    System.out.println("size:"+map.size()+";value:"+map.get("key1"));

打印信息：

size:2;value:value1
