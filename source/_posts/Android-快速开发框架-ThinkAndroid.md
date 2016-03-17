---
title: Android 快速开发框架 ThinkAndroid
tags: []
date: 2015-06-17 20:31:15
---

**ThinkAndroid简介
&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;**ThinkAndroid是一个免费的开源的、简易的、遵循Apache2开源协议发布的Android开发框
架，其开发宗旨是简单、快速的进行Android应用程序的开发，包含Android&nbsp;&nbsp;mvc、简易sqlite 
orm、ioc模块、封装Android&nbsp;&nbsp;httpclitent的http模块,具有快速构建文件缓存功能，无需考虑缓存文件的格式，都可以非常轻松
的实现缓存，它还基于文件缓存模块实现了图片缓存功能，在android中加载的图片的时候，对oom的问题，和对加载图片错位的问题都轻易解决。他还包
括了一个手机开发中经常应用的实用工具类，如日志管理，配置文件管理，android下载器模块，网络切换检测等等工具。&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; 
<!-- more -->
**目前ThinkAndroid主要有以下模块：**

*   MVC模块：实现视图与模型的分离。

*   ioc模块：android中的ioc模块，完全注解方式就可以进行UI绑定、res中的资源的读取、以及对象的初始化。

*   数据库模块：android中的orm框架，使用了线程池对sqlite进行操作。

*   http模块：通过httpclient进行封装http数据请求，支持异步及同步方式加载。

*   &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; 缓存模块：通过简单的配置及设计可以很好的实现缓存，对缓存可以随意的配置

*   &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; 图片缓存模块：imageview加载图片的时候无需考虑图片加载过程中出现的oom和android容器快速滑动时候出现的图片错位等现象。

*   &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; 配置器模块：可以对简易的实现配对配置的操作，目前配置文件可以支持Preference、Properties对配置进行存取。

*   &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; 日志打印模块：可以较快的轻易的是实现日志打印，支持日志打印的扩展，目前支持对sdcard写入本地打印、以及控制台打印

*   &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; 下载器模块:可以简单的实现多线程下载、后台下载、断点续传、对下载进行控制、如开始、暂停、删除等等。

*   &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; 网络状态检测模块：当网络状态改变时，对网络状态进行检测。

<span style="font-size: 24px;">下载地址：</span>[<span style="font-size: 24px;">http://pan.baidu.com/s/1dDjMHBb</span>](http://pan.baidu.com/s/1dDjMHBb)