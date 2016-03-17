---
title: Android高性能开发框架《KJFrameForAndroid》
tags: []
date: 2015-06-17 20:29:20
---

KJFrameForAndroid 又叫KJLibrary，是一个帮助快速开发的框架。使用KJFrameForAndroid，你可以只用一行代码就完成http请求、网络图片加载、数据库数据保存或读取。
KJFrameForAndroid 包含了几乎全部Android开发中必须的工具类。
KJFrameForAndroid 参考了许多国际上著名的Android框架如Volley、sync-http，上手使用门槛更低，更全面的http请求，考虑周全的bitmap网络加载，完善的功能且不受混淆影响...
KJFrameForAndroid 最低兼容android 3.0
<!-- more -->
很多朋友在问，KJFrameForAndroid与xUtils、afinal、thinkAndroid这类框架有什么区别，在你看过了这类框架的源代码后就会很直观的发现：**KJFrameForAndroid的项目结构与代码更加直观明了易懂，项目demo与API文档更加齐全，更关键的是使用起来更加简单易用，容易上手。**

===========================各模块介绍======================
**UILibrary模块**
UILibrary包含两个部分Widget(控件)、Topology(Android框架结构继承链)

UILibrary -&gt; Widget控件部分 
主要封装了常用的UI控件，为了不让项目jar包过大，我们只引入了开发中一定会用到的控件，例如：可上下拉的KJListView、可上下拉的
KJScrollView、可以双指缩放双击缩放双指旋转的ScaleImageView、等等......更多内容请自行查看项目文件中
org.kymjs.aframe.widget包下的内容
UILibrary -&gt; Topology拓扑部分 
包含一个使用IOC设计思想的控件初始化方式：可通过注解的方式进行UI绑定，与设置监听，在Activity和Fragment中均可以通过一行代码绑
定控件并实现点击监听；还包含了在目前应用开发中常见的布局界面，如侧滑效果，高效的底部TAB导航，3D效果的切换。同时UILibrary为开发者定
义了完善的BaseActivity和BaseFragment，开发者只需手动继承就可以获得Topology部分的全部功能。

**BitmapLibrary模块**
一行代码实现网络图片加载（可以是imageview或任何View）：kjb.display(view, &quot;http://xxx.xxx.xxx&quot;);
任何View(ImageView设置src，普通View设置bg)加载图片的时候都无需考虑图片加载过程中出现的oom和android容器快速滑动时候出现的图片错位等现象，同时无需考虑图片加载过程中出现的OOM。默认使用内存lru算法+磁盘lru算法缓存图片

**HttpLibrary模块**
可以一行代码实现Http请求：kjh.urlPost(&quot;http://www.eoeandroid.com&quot;, params, callback);
还可以一行代码实现文件或图片的上传与下载。 kjh.download( url, params, callback);
KJLibrary默认对所有Http通信的数据做了缓存处理，缓存时间为5分钟。这么做的目的不仅是为了节省用户手机流量，同时是为了减少服务器压力
HttpLibrary模块使用HttpClient与HttpUrlConnection两种实现方式实现网络通信、数据上传、多线程断点下载。

**DBLibrary模块**
可以一行代码对数据库进行增删改查等操作：kjdb.update(); kjdb.add(); .......
包含了android中的orm框架，使用了线程池对sqlite进行操作，一行代码就可以进行增删改查。支持一对多，多对一等查询。

github项目地址：
[https://github.com/kymjs/KJFrameForAndroid](https://github.com/kymjs/KJFrameForAndroid)
备用项目地址：
[http://git.oschina.net/kymjs/KJFrameForAndroid](http://git.oschina.net/kymjs/KJFrameForAndroid)