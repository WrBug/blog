---
title: jni 通过c/c++返回HashMap等复杂参数给java
tags: []
date: 2015-07-02 16:15:11
---

&nbsp; 返回其他对象与这个相似，可以自己研究下

思路：

&nbsp;&nbsp;&nbsp; 1.创建HashMap对象：
<pre class="brush:cpp;toolbar:false">&nbsp;&nbsp;&nbsp;&nbsp;/*C语言版本，下同*/
&nbsp;&nbsp;&nbsp;&nbsp;//获取java的HashMap类
&nbsp;&nbsp;&nbsp;jclass&nbsp;class_hashmap&nbsp;=&nbsp;(*env)-&gt;FindClass(env,&nbsp;&quot;java/util/HashMap&quot;);
&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;//获取类似于java&nbsp;的new&nbsp;HashMap();
&nbsp;&nbsp;&nbsp;&nbsp;jmethodID&nbsp;hashmap_init&nbsp;=&nbsp;(*env)-&gt;GetMethodID(env,&nbsp;class_hashmap,&nbsp;&quot;&lt;init&gt;&quot;,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;()V&quot;);
&nbsp;&nbsp;&nbsp;&nbsp;//初始化。类似于hashMap=new&nbsp;HashMap();
&nbsp;&nbsp;&nbsp;&nbsp;jobject&nbsp;HashMap&nbsp;=&nbsp;(*env)-&gt;NewObject(env,&nbsp;class_hashmap,&nbsp;hashmap_init,&nbsp;&quot;&quot;);
&nbsp;&nbsp;&nbsp;&nbsp;//获取hashMap.put()的ID
&nbsp;&nbsp;&nbsp;&nbsp;jmethodID&nbsp;HashMap_put&nbsp;=&nbsp;(*env)-&gt;GetMethodID(env,&nbsp;class_hashmap,&nbsp;&quot;put&quot;,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;&quot;);</pre>

&nbsp;&nbsp; 2\. 赋值：
<pre class="brush:cpp;toolbar:false;">&nbsp;&nbsp;&nbsp;&nbsp;//类似于map.put(&quot;key&quot;,&quot;value&quot;);
&nbsp;&nbsp;&nbsp;&nbsp;//(*env)-&gt;NewStringUTF(env,&nbsp;&quot;key值&quot;)不能直接用&quot;key值&quot;替代
&nbsp;&nbsp;(*env)-&gt;CallObjectMethod(env,&nbsp;HashMap,&nbsp;HashMap_put,&nbsp;(*env)-&gt;NewStringUTF(env,&nbsp;&quot;key值&quot;),&nbsp;(*env)-&gt;NewStringUTF(env,&nbsp;&quot;value值&quot;));</pre>

全部代码：

&nbsp;&nbsp;&nbsp;&nbsp;JniClient.java
<pre class="brush:java;toolbar:false">package&nbsp;com.ndk.test;
import&nbsp;java.util.HashMap;
public&nbsp;class&nbsp;JniClient&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;public&nbsp;static&nbsp;native&nbsp;HashMap&lt;String,&nbsp;String&gt;&nbsp;setMap();
}</pre>

JniClient.h
<pre class="brush:cpp;toolbar:false">/*&nbsp;DO&nbsp;NOT&nbsp;EDIT&nbsp;THIS&nbsp;FILE&nbsp;-&nbsp;it&nbsp;is&nbsp;machine&nbsp;generated&nbsp;*/
#include&nbsp;&lt;jni.h&gt;
/*&nbsp;Header&nbsp;for&nbsp;class&nbsp;com_ndk_test_JniClient&nbsp;*/
#ifndef&nbsp;_Included_com_ndk_test_JniClient
#define&nbsp;_Included_com_ndk_test_JniClient
#ifdef&nbsp;__cplusplus
extern&nbsp;&quot;C&quot;&nbsp;{
#endif
/*
&nbsp;*&nbsp;Class:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;com_ndk_test_JniClient
&nbsp;*&nbsp;Method:&nbsp;&nbsp;&nbsp;&nbsp;setMap
&nbsp;*&nbsp;Signature:&nbsp;()Ljava/util/HashMap;
&nbsp;*/
JNIEXPORT&nbsp;jobject&nbsp;JNICALL&nbsp;Java_com_ndk_test_JniClient_setMap
&nbsp;&nbsp;(JNIEnv&nbsp;*,&nbsp;jclass);
#ifdef&nbsp;__cplusplus
}
#endif
#endif</pre>

JniClient.c
<pre class="brush:cpp;toolbar:false">#include&nbsp;&quot;com_ndk_test_JniClient.h&quot;
#include&lt;stdio.h&gt;
#ifdef&nbsp;__cplusplus
extern&nbsp;&quot;C&quot;
{
#endif
JNIEXPORT&nbsp;jobject&nbsp;JNICALL&nbsp;Java_com_ndk_test_JniClient_setMap(JNIEnv&nbsp;*env,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;jclass&nbsp;cls)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;jclass&nbsp;class_hashmap&nbsp;=&nbsp;(*env)-&gt;FindClass(env,&nbsp;&quot;java/util/HashMap&quot;);
&nbsp;&nbsp;&nbsp;&nbsp;jmethodID&nbsp;hashmap_init&nbsp;=&nbsp;(*env)-&gt;GetMethodID(env,&nbsp;class_hashmap,&nbsp;&quot;&lt;init&gt;&quot;,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;()V&quot;);
&nbsp;&nbsp;&nbsp;&nbsp;jobject&nbsp;HashMap&nbsp;=&nbsp;(*env)-&gt;NewObject(env,&nbsp;class_hashmap,&nbsp;hashmap_init,&nbsp;&quot;&quot;);
&nbsp;&nbsp;&nbsp;&nbsp;jmethodID&nbsp;HashMap_put&nbsp;=&nbsp;(*env)-&gt;GetMethodID(env,&nbsp;class_hashmap,&nbsp;&quot;put&quot;,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;&quot;);
&nbsp;&nbsp;&nbsp;&nbsp;(*env)-&gt;CallObjectMethod(env,&nbsp;HashMap,&nbsp;HashMap_put,&nbsp;(*env)-&gt;NewStringUTF(env,&nbsp;&quot;key1&quot;),&nbsp;(*env)-&gt;NewStringUTF(env,&nbsp;&quot;value1&quot;));
&nbsp;&nbsp;&nbsp;&nbsp;(*env)-&gt;CallObjectMethod(env,&nbsp;HashMap,&nbsp;HashMap_put,(*env)-&gt;NewStringUTF(env,&nbsp;&quot;key2&quot;),&nbsp;(*env)-&gt;NewStringUTF(env,&nbsp;&quot;value2&quot;));
&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;HashMap;
}
#ifdef&nbsp;__cplusplus
}
#endif</pre>

引用方法：

<pre class="brush:java;toolbar:false">Object&nbsp;object=JniClient.setMap();
HashMap&lt;String,&nbsp;String&gt;map=(HashMap&lt;String,&nbsp;String&gt;)object;
System.out.println(&quot;size:&quot;+map.size()+&quot;;value:&quot;+map.get(&quot;key1&quot;));</pre>

打印信息：

size:2;value:value1