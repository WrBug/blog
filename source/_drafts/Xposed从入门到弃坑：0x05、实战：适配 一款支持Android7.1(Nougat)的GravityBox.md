---
title: Xposed从入门到弃坑：0x05、实战：适配一款支持Android7.1(Nougat)的GravityBox 插件
date: 2017-07-10 19:38:34
categories:
- xposed开发
tags: 
- Xposed
- GravityBox
- 移植
---

前几天，国外大神发布了Android7.1 的Xposed框架，作为热衷于Xposed人的来说，肯定是第一时间把系统升级到Android7.1(后文用Nougat代替)，刷入Xposed框架了。毕竟谷歌亲儿子，升级系统还是比较方便的。
升级成功后才发现竟然没有支持Nougat的GravityBox，哎我这暴脾气就看不下去了。果断下载其源码。开始做适适配。
Nougat的Xposed框架下载： [Xposed Android 7.1 Nougat 版本框架发布][1]

<!--more-->

重力工具箱GravityBox是一款依赖Xposed框架支持的全能系统工具，支持修改rom的部分系统级重要参数。由于Nougat版本的Xposed发布比较晚，作者还并未做适配。求人不如求己，那就自己做一个适配。

> GravityBox is a module which primary goal is to provide the users of MediaTek platform (which is well known for not being opensource friendly)
with a tweak box to turn their vanilla Android stock ROM into custom ROM packed with additional features and tweaks.
Additionally, it should run on any device having vanilla or close to vanilla Android not diverting too much from AOSP (Android Open Source Project).

上面是官方介绍，更多的可以访问下方的链接：

[https://forum.xda-developers.com/xposed/modules/app-gravitybox-v6-0-0-tweak-box-android-t3251148][2]

[https://github.com/GravityBox/GravityBox][3]

### 准备工作

在GitHub上面将GravityBox拉到本地，用AndroidStudio打开，为了减少差异性。选择marshmallow分支进行适配，由于适配需要对照着marshmallow和Nougat的源码进行，所以需要Android官网查看源码。具体怎么访问官网，你们懂得。下面提供了marshmallow和Nougat的源码地址，具体怎么使用，后面会讲到。


**marshmallow源码：**
[https://android.googlesource.com/platform/frameworks/base.git/+/android-6.0.1_r80][4]
**Nougat源码：**
[https://android.googlesource.com/platform/frameworks/base/+/android-7.1.2_r27][5]







[1]: /2017/07/20/Xposed_Android7.0版本框架发布/
[2]: https://forum.xda-developers.com/xposed/modules/app-gravitybox-v6-0-0-tweak-box-android-t3251148
[3]: https://github.com/GravityBox/GravityBox
[4]: https://android.googlesource.com/platform/frameworks/base.git/+/android-6.0.1_r80
[5]: https://android.googlesource.com/platform/frameworks/base/+/android-7.1.2_r27