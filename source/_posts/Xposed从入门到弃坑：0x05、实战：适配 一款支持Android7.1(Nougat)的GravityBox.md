---
title: Xposed从入门到弃坑：0x05、实战：适配一款支持Android7.1(Nougat)的GravityBox 插件
date: 2017-07-22 10:33:55
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

## 准备工作

在GitHub上面将GravityBox拉到本地，用AndroidStudio打开，为了减少差异性。选择marshmallow分支进行适配，由于适配需要对照着marshmallow和Nougat的源码进行，所以需要Android官网查看源码。具体怎么访问官网，你们懂得。下面提供了marshmallow和Nougat的源码地址，具体怎么使用，后面会讲到。


**Marshmallow源码：**
[https://android.googlesource.com/platform/frameworks/base.git/+/android-6.0.1_r80][4]
**Nougat源码：**
[https://android.googlesource.com/platform/frameworks/base/+/android-7.1.2_r27][5]


## START

做软件移植最主要的是比较差异性。在GravityBox中应用了大量的反射，所以就需要对照源码进行。下面通过一个例子来讲解。在是配置需要大量的重启设备，因为需要重启才会生效

<font color='red'>注意：在移植过程中，手机可能会无法进入桌面。解决方案有两个：</br>1. 连接上adb，通过adb重新安装GravityBox。通过`adb reboot`重启</br>2.  通过adb shell 模式删除 /data/data/xx.xx(GravityBox包名)/share_prefs下所有文件，无法开机可以在recovery模式下使用该方法。重启</br>移植有风险。需谨慎
</font>

### 修改基本配置

工程直接打包是不能在Nougat运行的，元澳门做了版本限制，需要修改部分配置，教程以AndroidStudio工程进行讲解，使用手机为nexus6p。
- 修改build.gradle

``` gradle
apply plugin: 'com.android.application'
android {
    compileSdkVersion 23
    buildToolsVersion "25.0.3"

    defaultConfig {
        applicationId "com.wrbug.gravitybox.nougat"
        minSdkVersion 25
        targetSdkVersion 23
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.txt'
        }
    }
}


dependencies {
    provided 'de.robv.android.xposed:api:82'
}
```
compileSdkVersion和targetSdkVersion用23，因为用25会crash，主要原因是安全机制引起的。minSdkVersion选择25，添加xposed的依赖

- 修改Xposed入口版本检测
查看xposed_init文件可以发现入口为GravityBox类，在类里有一些做Android版本检测的判断:
`Build.VERSION.SDK_INT != 23`，将判断改成`Build.VERSION.SDK_INT != 25`。

修改完后直接编译运行，Xposed激活后重启

### 开启清除所有最近使用的应用程序

重启完成后，可以发现能进设置页了。如下图所示，但是只有部分功能有用.

![][7]

进入杂项调整->清除所有最近使用的应用程序,选择一个选项。我选择的是右下角，选好后切到任务栏(就是显示打开了哪些应用的那个页面)，并没有出现那个按钮，查看下androidstudio的日志，发现有个报错的信息：

``` java
java.lang.NoSuchFieldError: com.android.systemui.recents.RecentsActivity#mConfig
		at de.robv.android.xposed.XposedHelpers.findField(XposedHelpers.java:102)
		at de.robv.android.xposed.XposedHelpers.getObjectField(XposedHelpers.java:848)
		at com.wrbug.gravitybox.nougat.ModClearAllRecents$4.afterHookedMethod(ModClearAllRecents.java:290)
		at de.robv.android.xposed.XposedBridge.handleHookedMethod(XposedBridge.java:348)
		at android.app.Activity.onResume(Unknown Source)
		at android.app.Instrumentation.callActivityOnResume(Instrumentation.java:1269)
		at android.app.Activity.performResume(Activity.java:6783)
		at android.app.ActivityThread.performResumeActivity(ActivityThread.java:3406)
		at android.app.ActivityThread.handleResumeActivity(ActivityThread.java:3469)
		at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1527)
		at android.os.Handler.dispatchMessage(Handler.java:102)
		at android.os.Looper.loop(Looper.java:154)
		at android.app.ActivityThread.main(ActivityThread.java:6119)
		at java.lang.reflect.Method.invoke(Native Method)
		at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:886)
		at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:776)
		at de.robv.android.xposed.XposedBridge.main(XposedBridge.java:102)
```

提示NoSuchFieldError错误。没有找到相应的字段，报错的代码为：

``` java
Object config = XposedHelpers.getObjectField(param.thisObject, "mConfig");
```
进入我上面提供的源码网址，找到com.android.systemui.recents.RecentsActivity类所在的位置。有的同学可能不会找。我提供一种简单的方案，使用google搜索*com.android.systemui.recents.RecentsActivity*，进入第一个页面：

![][8]

里面可以查看该类所在的目录，然后在我提供的源码网址找到相应的目录即可。有些位置会不一样，比如就这个类。在Marshmallow(后文用M代替)中的位置在：`/packages/SystemUI/src/com/android/systemui/recents/RecentsActivity.java`，Nougat（后文用N代替）的目录也一样，现在来比较两个文件的差异，报错提示mConfig字段未找到，M中的字段定义为：`RecentsConfiguration mConfig;`，但是在N中没有这个。回到GravityBox的源码中，先看看报错的地方做了什么骚操作

``` java
Object config = XposedHelpers.getObjectField(param.thisObject, "mConfig");
boolean hasTasks = !XposedHelpers.getBooleanField(config, "launchedWithNoRecentTasks");
```
只是获取了launchedWithNoRecentTasks字段，那就要想办法在N上面获取到这个值。在M里，分析RecentsConfiguration类，在源码的304行有这个值的返回，在返回到RecentsActivity，发现并没有使用到该方法。下面就要看看mConfig在哪里有用到了，通过网页查找关键字发现，只有363行的`mScrimViews = new SystemBarScrimViews(this, mConfig);`把该对象传了过去，并且对比发现N的RecentsActivity也有mScrimViews字段，都是SystemBarScrimViews的实例。不过生成的方式不一样，在N中的325行的实现为：`mScrimViews = new SystemBarScrimViews(this);`，接下来试试将这里作为突破口。

``` java
    /** Returns whether the status bar scrim should be visible. */
    public boolean hasStatusBarScrim() {
        return !launchedWithNoRecentTasks;
    }
    /** Returns whether the nav bar scrim should be visible. */
    public boolean hasNavBarScrim() {
        // Only show the scrim if we have recent tasks, and if the nav bar is not transposed
        return !launchedWithNoRecentTasks && (!hasTransposedNavBar || !isLandscape);
    }
```
打开N和M的SystemBarScrimViews类，对比下源码：

``` java
/**
 *Marshmallow源码
 */
public void prepareEnterRecentsAnimation() {
	//调用hasNavBarScrim（）
	mHasNavBarScrim = mConfig.hasNavBarScrim();
	mShouldAnimateNavBarScrim = mConfig.shouldAnimateNavBarScrim();
	
	//调用hasStatusBarScrim（）
	mHasStatusBarScrim = mConfig.hasStatusBarScrim();
	mShouldAnimateStatusBarScrim = mConfig.shouldAnimateStatusBarScrim();
	mNavBarScrimView.setVisibility(mHasNavBarScrim && !mShouldAnimateNavBarScrim ?
			View.VISIBLE : View.INVISIBLE);
	mStatusBarScrimView.setVisibility(mHasStatusBarScrim && !mShouldAnimateStatusBarScrim ?
			View.VISIBLE : View.INVISIBLE);
}


	
/**
 * Nougat源码
 */
public void updateNavBarScrim(boolean animateNavBarScrim, boolean hasStackTasks,
		AnimationProps animation) {
	prepareEnterRecentsAnimation(isNavBarScrimRequired(hasStackTasks), animateNavBarScrim);
	if (animateNavBarScrim && animation != null) {
		animateNavBarScrimVisibility(true, animation);
	}
}


private void prepareEnterRecentsAnimation(boolean hasNavBarScrim, boolean animateNavBarScrim) {
	mHasNavBarScrim = hasNavBarScrim;
	mShouldAnimateNavBarScrim = animateNavBarScrim;
	mNavBarScrimView.setVisibility(mHasNavBarScrim && !mShouldAnimateNavBarScrim ?
			View.VISIBLE : View.INVISIBLE);
}

private boolean isNavBarScrimRequired(boolean hasStackTasks) {
	return hasStackTasks && !mHasTransposedNavBar && !mHasDockedTasks;
}
```
猜测isNavBarScrimRequired方法的传参就是GravityBox需要的值，只需要hook到该方法。获取hasStackTasks的值即可。

其他报错信息可以通过类似的方法进行修正，我也开源了自己移植的版本，会持续进行，欢迎大家star和提交pullrequest

### 项目地址

[https://github.com/WrBug/GravityBox][6]

[1]: /2017/07/20/Xposed_Android7.0版本框架发布/
[2]: https://forum.xda-developers.com/xposed/modules/app-gravitybox-v6-0-0-tweak-box-android-t3251148
[3]: https://github.com/GravityBox/GravityBox
[4]: https://android.googlesource.com/platform/frameworks/base.git/+/android-6.0.1_r80
[5]: https://android.googlesource.com/platform/frameworks/base/+/android-7.1.2_r27
[6]: https://github.com/WrBug/GravityBox
[7]: /upload/2017/07/20170722-112125.png
[8]: /upload/2017/07/20170722-115352.png