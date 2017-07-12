---
title: Xposed从入门到弃坑：0x04、实战：某段子App应用内广告屏蔽
date: 2017-07-10 19:38:34
categories:
- xposed开发
tags: 
- Xposed
- 广告屏蔽

---

前面三节对Xposed做了简要的介绍和一些用法的简单描述，这篇将讲解怎样通过Xposed框架对某段子app的广告进行屏蔽。这篇文章已假设你已经了解了Xposed的用法。还不清楚的请回看前面的内容
<!-- more -->
## 1 准备工具
1. 待屏蔽的App：[内涵段子v6.4.6][1]  （由于app会进行混淆。所以每个版本的包都会有差异）
2. 反编译工具：dex2jar
3. jar文件查看工具：jd-gui 或者 Luyten
4. 抓包工具：Charles ,fiddler,wireshark
5. 已经安装Xposed插件的手机
6. Android Device Monitor（Android studio自带有。Tools->Android->Android Device Monitor）

## 2 屏蔽套路
Xposed插件开发并没有什么固定的套路，可能会有很多种方式，我只提供我的一种方式。<font color='red'>网络抓包+黑盒测试+人品</font>。听起来很高大上的样子，确实，听起来是的🌚 
黑盒测试可以方便的获取到源码中所需要的东西，避免用直接通过查看源码的方式查找

## STARTED

### 申明

本文仅通过内涵段子App为例作为教程对Xposed进行学习，请勿作为它用，本课程也不提供全部源码，本文代码使用的是**kotlin**语言，毕竟转正了。内涵段子官网：[http://neihanshequ.com/][2]

### 黑盒分析：界面布局
首先下载好内涵段子，打开应用，为了方便查看，切到段子栏，刷新下数据，然后就会出现广告，如图

![][3]  

打开Android Device Monitor对该页面进行分析，发现该页面的容器为listview，广告也是作为一个Item添加进去的。

![][4]

而每个listview的Item是通过setAdapter()设置，听到这里，是不是有点想法了😏。没错，是要拿到这个adapter是怎么实现的，那又怎么才能拿到呢？那必须是要通过xposed框架hook到setAdapter的方法。先看看setAdapter方法的定义：

```java
    @Override
    public void setAdapter(ListAdapter adapter) {
    }
```
在listview中重写了该方法，所以需要hook listview的setAdapter，传参为ListAdapter，hook的代码如下：


``` kotlin

class XposedInit : IXposedHookLoadPackage {
    companion object {
        val JOKE_PACKAGE_NAME = "com.ss.android.essay.joke"
    }

    override fun handleLoadPackage(lpparam: XC_LoadPackage.LoadPackageParam?) {
        if (!lpparam?.packageName.equals(JOKE_PACKAGE_NAME)) {
            return
        }
        XposedHelpers.findAndHookMethod("android.widget.ListView", lpparam?.classLoader, "setAdapter", Class.forName("android.widget.ListAdapter"), object : XC_MethodHook() {
            override fun afterHookedMethod(param: MethodHookParam?) {
                if (param?.thisObject is ListView) {
                    XposedBridge.log(param.args[0].toString())
                }
            }
        })
    }
}

```
方式很简单。获取到ListAdapter实例，打印class。其中param.args为一个object数组，表示该方法的参数，安装到手机后，重启手机，启动内涵段子。在logcat中筛选出Xposed的log，注意下面这一行：

`07-10 17:50:59.908 5669-5669/? I/Xposed: com.ss.android.essay.base.feed.adapter.multipart.b.t@2ccfb40`

这一行就是adapter的类。


### 抓包分析：列表数据分析

打开抓包工具，设置好手机代理，抓取带广告的列表数据,我选择的是wireshark抓包工具，筛选`tcp&&ip.addr==手机ip`，抓取的数据包我也已经上传，可以直接下载用wireshark载入，[点击下载][5]。筛选`tcp&&ip.addr==10.1.133.204`，app内刷新数据，可以在14行看到一条关键数据请求：
`14	0.413437 10.1.133.204 10.1.133.181 HTTP 1310
GET http://is.snssdk.com/neihan/stream/mix/v1/?mpic=1&webp=1&essence=1 HTTP/1.1 `

在95行有数据返回，该数据即为列表，有些则包含了广告
`95	2.788098	10.1.133.181	10.1.133.204	HTTP	71	HTTP/1.1 200 OK  (application/json)`
数据为json，首先分析json的格式。将返回的数据，在wireshark中显示分组字节即可将数据复制出来，不会的话我上传了完整的数据,跟数据包在同一个压缩文件里，json格式如下：

```json

{
    "message": "success",
    "data": {
        "has_more": false,
        "tip": "",
        "has_new_message": false,
        "max_time": 1499741399,
        "min_time": 1499742064,
        "data": [
            {
                "group": {
                    "type": 3
                },
                "comments": [
                    {}
                ],
                "type": 1,
                "display_time": 1499741994,
                "online_time": 1499741994
            },
            {
                "online_time": 1499741960,
                "display_time": 1499741960,
                "type": 5,
                "ad": {}
            }
        ]
    }
}

```

为了方便，我删除了无用的信息。在json中，最下面的data数组即为列表的数据，哦保留了两条数据，第一条为正常的数据，其中type=3，第二天为广告，type=5，ad字段为广告对象。首先尝试在源码里寻找type==5 的关键字

### 人品分析：源码分析

首先将dex转为jar文件，通过jar查看工具查看在上面通过hook找到的adapter类，搜索关键字： `== 5`或者其他类似的。果然，在源码504行出现了以下代码：

```java
else if (c.b == 5 && c.d != null && c.d instanceof EssayAd) {
    list2.add((y.a)new com.ss.android.essay.base.feed.adapter.multipart.b.e(c, this.d, this.n, this.l, this.h, this.z, (ah)this, this.u));
}
```
通过`c.d instanceof EssayAd`猜测这里就是添加广告的地方，在找到这几行所在的方法：

``` java
@Override
protected List<y.a> a(final com.ss.android.essay.base.feed.data.c c) {}
```
如果上面的猜测正确的话，只需要不让代码进入if里面就好了。

### Xposed实现

通过hook adapter里面的a方法，获取c参数，判断c.b==5，如果想等。将c.d置为null即可。代码如下：

```kotlin 
XposedHelpers.findAndHookMethod("com.ss.android.essay.base.feed.adapter.multipart.b.t", lpparam?.classLoader, "a", lpparam?.classLoader?.loadClass("com.ss.android.essay.base.feed.data.c"), object : XC_MethodHook() {
    override fun beforeHookedMethod(param: MethodHookParam?) {
        val type = XposedHelpers.getIntField(param!!.args[0], "b")
        var dField = XposedHelpers.findField(param.args[0]::class.java, "d")
        if (type == 5 && dField != null) {
            XposedBridge.log("广告已屏蔽")
            dField.set(param.args[0], null)
        }
    }
})
```
安装后重启手机，打开app，可以发现广告已经屏蔽，log里面也有“广告已屏蔽” 的日志


[1]: /upload/2017/07/neihanduanzi_646.apk
[2]: http://neihanshequ.com/
[3]: /upload/2017/07/20170710-200226@2x.png
[4]: /upload/2017/07/20170710-181953.png
[5]: /upload/2017/07/数据包.zip
