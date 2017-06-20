---
title: Xposed从入门到弃坑：0x02、IXposedHook相关接口解析
date: 2017-04-26 16:00:29
categories:
- xposed开发
tags: 
- xposed

---

在上一篇文章中我们通过一个简单的例子开发了一款Xposed框架，感受到了Xposed的强大功能，在demo中我们新建了一个XposedInit的类实现了IXposedHookLoadPackage 接口，在handleLoadPackage中进行hook，最终达到了我们的目的，那IXposedHookLoadPackage是干什么的呢？还有handleLoadPackage什么时候会调用呢？还有IXposedHookInitPackageResources和IXposedHookZygoteInit的左右是什么？这期会做一个讲解。对上一篇文章有遗忘的可以回过头在看一遍：[Xposed从入门到弃坑：一、Xposed初探][1]
<!--more-->
## IXposedHookLoadPackage
从字面上翻译就是在加载包时开始hook。接口需要实现*handleLoadPackage*方法，该方法会在执行Application.onCreate()方法前调用，并且携带一个*XC_LoadPackage.LoadPackageParam lpparam*返回过来，lpparam包含了hook到的应用的一些信息，具体通过表格来说明 **（表格的description均为hook到的应用相关信息，不是Xposed项目的信息）**

|  fields   |  type   |  description   |
| --- | --- | --- |
| packageName    |  String   |   应用包名  |
|  processName   |  String   |  应用加载后的进程名   |
|  classLoader   |  ClassLoader   |  应用的classloader   |
|   appInfo  |  ApplicationInfo   |  应用的信息，包括verisonCode，uid等|

表格只是简单的介绍，具体需要再今后的开发中再讲解，在上篇文章中，在hook到方法后，使用反射获取textview，再来回顾下代码：

``` java
//不能通过Class.forName()来获取Class ，在跨应用时会失效
Class c=lpparam.classLoader.loadClass("com.wrbug.xposeddemo.MainActivity");
Field field=c.getDeclaredField("textView");
field.setAccessible(true);
//param.thisObject 为执行该方法的对象，在这里指MainActivity
TextView textView= (TextView) field.get(param.thisObject);
textView.setText("Hello Xposed");
```
在第一行中 class没有用Class.forName()来获取，是什么原因呢？我们先来看看Class.forName()的源码：
``` java
    @CallerSensitive
    public static Class<?> forName(String className) throws ClassNotFoundException {
        return forName(className, true, VMStack.getCallingClassLoader());
    }
	
	@CallerSensitive
    public static Class<?> forName(String name, boolean initialize, ClassLoader loader) throws ClassNotFoundException {
        if (loader == null) {
            loader = BootClassLoader.getInstance();
        }
        Class<?> result;
        try {
            result = classForName(name, initialize, loader);
        } catch (ClassNotFoundException e) {
            Throwable cause = e.getCause();
            if (cause instanceof LinkageError) {
                throw (LinkageError) cause;
            }
            throw e;
        }
        return result;
    }

    /** Called after security checks have been made. */
    static native Class<?> classForName(String className, boolean shouldInitialize, ClassLoader classLoader) throws ClassNotFoundException;
```
在三个参数的方法中，有一个需要传一个ClassLoader进去，在一个参数的方法中，ClassLoader是通过VMStack.getCallingClassLoader()获取的。VMStack是一个虚拟机栈，在Android系统中，每个应用都有一个独立的虚拟机，所以VMStack.getCallingClassLoader()是获取当前应用的ClassLoader，即xposed项目的ClassLoader，所以，如果使用`Class.forName("xxx.xxx.xxxActivity")`获取不同应用的类会提示找不到，这就是需要通过`lpparam.classLoader.loadClass()`获取的原因。

## IXposedHookInitPackageResources
这个是在资源布局初始化时进行hook，需要实现`handleInitPackageResources(XC_InitPackageResources.InitPackageResourcesParam resparam)` 方法，在初始化时调用，resparam有以下两个字段：

|  field   |   type  |  description   |
| --- | --- | --- |
|  packageName   |  String   |   应用包名  |
|   res  |  XResources   |  资源相关   |

resparam.res是一个非常重要的字段，里面包含了很多资源的信息，并且继承Resources。下面通过一个例子做个简要的说明。还是使用上期的demo，项目地址：[https://github.com/WrBug/XposedDemo][2] ， 命令切换到提交：

``` vim
git checkout 0be008e
```
demo为在R.layout.activity_main布局初始化时进行hook，打印出hook到的view。布局做些修改，多加几个控件：

``` xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context="com.wrbug.xposeddemo.MainActivity">

    <TextView
        android:id="@+id/textview"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent"/>

    <Button
        android:id="@+id/button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Button"/>

    <RatingBar
        android:id="@+id/ratingBar"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"/>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical">

        <Switch
            android:id="@+id/switch1"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Switch"/>

        <ListView
            android:layout_width="match_parent"
            android:layout_height="match_parent"/>
    </LinearLayout>

</LinearLayout>

```

在Activity的onCreate里面加入两个log：

``` java
  @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.i("Xposed", "before setcontent");
        setContentView(R.layout.activity_main);
        Log.i("Xposed", "after setcontent");
        textView = (TextView) findViewById(R.id.textview);
        textView.setText("WrBug");

        Log.i("Xposed", "before inflate");
        getLayoutInflater().inflate(R.layout.view_demo, null);
        Log.i("Xposed", "after inflate");
    }
```
也就是在setContentView两边加了before setcontent和after setcontent两个log，添加一个inflate布局的方法，接下来在XposenInit里面实现IXposedHookInitPackageResources接口，并且实现`handleInitPackageResources(XC_InitPackageResources.InitPackageResourcesParam resparam)` 方法，代码如下：

``` java
public class XposedInit implements IXposedHookLoadPackage, IXposedHookInitPackageResources {
    @Override
    public void handleLoadPackage(final XC_LoadPackage.LoadPackageParam lpparam) {
        if (lpparam.packageName.equals("com.wrbug.xposeddemo")) {
            XposedHelpers.findAndHookMethod("com.wrbug.xposeddemo.MainActivity", lpparam.classLoader, "onCreate", Bundle.class, new XC_MethodHook() {
                @Override
                protected void afterHookedMethod(MethodHookParam param) throws Throwable {
                    //不能通过Class.forName()来获取Class ，在跨应用时会失效
                    Class c = lpparam.classLoader.loadClass("com.wrbug.xposeddemo.MainActivity");
                    Field field = c.getDeclaredField("textView");
                    field.setAccessible(true);
                    //param.thisObject 为执行该方法的对象，在这里指MainActivity
                    TextView textView = (TextView) field.get(param.thisObject);
                    textView.setText("Hello Xposed");
                }
            });
        }
    }

    @Override
    public void handleInitPackageResources(XC_InitPackageResources.InitPackageResourcesParam resparam) throws Throwable {
        if (resparam.packageName.equals("com.wrbug.xposeddemo")) {
            resparam.res.hookLayout(resparam.packageName, "layout", "activity_main", new XC_LayoutInflated() {
                @Override
                public void handleLayoutInflated(LayoutInflatedParam liparam) throws Throwable {
                    printView((ViewGroup) liparam.view, 1);
                }
            });
            resparam.res.hookLayout(resparam.packageName, "layout", "view_demo", new XC_LayoutInflated() {
                @Override
                public void handleLayoutInflated(LayoutInflatedParam liparam) throws Throwable {
                    XposedBridge.log("hook view_demo");
                }
            });
        }
    }
    //遍历资源布局树，并打印出来
    private void printView(ViewGroup view, int deep) {
        String viewgroupDeepFormat = "";
        String viewDeepFormat = "";
        for (int i = 0; i < deep - 1; i++) {
            viewgroupDeepFormat += "\t";
        }
        viewDeepFormat = viewgroupDeepFormat + "\t";
        XposedBridge.log(viewgroupDeepFormat + view.toString());
        int count = view.getChildCount();
        for (int i = 0; i < count; i++) {
            if (view.getChildAt(i) instanceof ViewGroup) {
                printView((ViewGroup) view.getChildAt(i), deep + 1);
            } else {
                XposedBridge.log(viewDeepFormat + view.getChildAt(i).toString());
            }
        }
    }
}
```
安装重启后，打开demo，查看打印的日志：

``` verilog
04-26 23:24:52.123 1818-1818/com.wrbug.xposeddemo I/Xposed: before setcontent
04-26 23:24:52.183 1818-1818/com.wrbug.xposeddemo I/Xposed: android.support.v7.widget.ContentFrameLayout{2fb5cbd7 V.E..... ......I. 0,0-0,0 #1020002 android:id/content}
04-26 23:24:52.183 1818-1818/com.wrbug.xposeddemo I/Xposed: 	android.widget.LinearLayout{33cd7cc4 V.E..... ......I. 0,0-0,0}
04-26 23:24:52.183 1818-1818/com.wrbug.xposeddemo I/Xposed: 		android.support.v7.widget.AppCompatTextView{2e1a07ad V.ED.... ......ID 0,0-0,0 #7f0b005e app:id/textview}
04-26 23:24:52.183 1818-1818/com.wrbug.xposeddemo I/Xposed: 		android.support.v7.widget.AppCompatButton{2c3a2ae2 VFED..C. ......I. 0,0-0,0 #7f0b005f app:id/button}
04-26 23:24:52.183 1818-1818/com.wrbug.xposeddemo I/Xposed: 		android.support.v7.widget.AppCompatRatingBar{1aa14e73 VFED.... ......ID 0,0-0,0 #7f0b0060 app:id/ratingBar}
04-26 23:24:52.183 1818-1818/com.wrbug.xposeddemo I/Xposed: 		android.widget.LinearLayout{1c87a130 V.E..... ......I. 0,0-0,0}
04-26 23:24:52.184 1818-1818/com.wrbug.xposeddemo I/Xposed: 			android.widget.Switch{13fc71a9 VFED..C. ......I. 0,0-0,0 #7f0b0061 app:id/switch1}
04-26 23:24:52.184 1818-1818/com.wrbug.xposeddemo I/Xposed: 			android.widget.ListView{3ed4132e V.ED.VC. ......I. 0,0-0,0}
04-26 23:24:52.184 1818-1818/com.wrbug.xposeddemo I/Xposed: after setcontent
04-26 23:24:52.184 1818-1818/com.wrbug.xposeddemo I/Xposed: before inflate
04-26 23:24:52.184 1818-1818/com.wrbug.xposeddemo I/Xposed: hook view_demo
04-26 23:24:52.184 1818-1818/com.wrbug.xposeddemo I/Xposed: after inflate
```
日志可以看出handleInitPackageResources会在`setContentView(R.layout.activity_main);`和`getLayoutInflater().inflate(R.layout.view_demo, null);`时调用。对setContentView有了解的都明白setContentView也会调用inflate方法。所以，也可以看成是hook了inflate方法。在返回的数据`XC_InitPackageResources.InitPackageResourcesParam resparam`中，有一个 `liparam.view`的字段，通过日志可以看出setContentView方法的是一个ContentFrameLayout，下面包含了LinearLayout，这个LinearLayout也就是我们activity_main布局最外层的view，获取到这个view以后就可以进行一系列的操作了。


  [1]: /2017/04/25/Xposed从入门到弃坑：一、Xposed初探/
  [2]: https://github.com/WrBug/XposedDemo