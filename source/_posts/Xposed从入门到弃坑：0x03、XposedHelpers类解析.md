---
title: Xposed从入门到弃坑：0x03、XposedHelpers类解析
date: 2017-06-29 16:09:15
categories:
- xposed开发
tags: 
- xposed
---

感觉好久没更新xposed教程了。应该有两个月了，主要是工作太忙，没有时间写博客。这节主要讲解XposedHelpers类的一些用法，对前面内容有遗忘的可以再回过去预习下。
<!--more-->

## XposedHelpers类是干嘛的？
在XposedHelpers类的顶部有一句注释

``` java
/**
 * Helpers that simplify hooking and calling methods/constructors, getting and settings fields, ...
 */
public final class XposedHelpers {
}
```
大概意思是可以hook活着调用方法/构造函数。获取该类的字段等。这里需要用到反射的姿势。不了解的可以先看看反射相关的。XposedHelpers提供了非常方便的或者这些参数的方法。

## XposedHelpers方法说明

``` java
//className  完整类名，classLoader 类加载器（app应用的类加载器）
public static Class<?> findClass(String className, ClassLoader classLoader)

public static Class<?> findClassIfExists(String className, ClassLoader classLoader)
```
获取class的方法。其中findclass方法在未找到时抛出异常，findClassIfExists则返回null

***

``` java

// clazz 通过findClass获取,调用findFieldRecursiveImpl获取
public static Field findField(Class<?> clazz, String fieldName)

public static Field findFieldIfExists(Class<?> clazz, String fieldName)

private static Field findFieldRecursiveImpl(Class<?> clazz, String fieldName) throws NoSuchFieldException {
		try {
			return clazz.getDeclaredField(fieldName);
		} catch (NoSuchFieldException e) {
			while (true) {
				clazz = clazz.getSuperclass();
				if (clazz == null || clazz.equals(Object.class))
					break;

				try {
					return clazz.getDeclaredField(fieldName);
				} catch (NoSuchFieldException ignored) {}
			}
			throw e;
		}
	}
	
public static Field findFirstFieldByExactType(Class<?> clazz, Class<?> type)

//获取实例字段的引用
public static Object getObjectField(Object obj, String fieldName)
```

获取Field的方法，具体实现是在findFieldRecursiveImpl方法里面获取，外部不能访问，<font color='red'>Field是通过getDeclaredField获取，所以只能获取static类型的字段</font>。indFirstFieldByExactType()方法是匹配Field的classType,如果类型一样，则返回该字段，该方法的局限性是只能获取到第一个匹配到的字段，后面相同类型的无法获取

***

``` java
public static Method findMethodExact(Class<?> clazz, String methodName, Object... parameterTypes) 

public static Method findMethodExactIfExists(Class<?> clazz, String methodName, Object... parameterTypes)

```
获取Method方法，还有些其他的方法这里省略，也只能获取静态方法

***

``` java
public static Constructor<?> findConstructorExact(Class<?> clazz, Object... parameterTypes)

public static Constructor<?> findConstructorExactIfExists(Class<?> clazz, Object... parameterTypes) 

public static Constructor<?> findConstructorBestMatch(Class<?> clazz, Class<?>... parameterTypes)
```
获取Constructor方法，其中Object... parameterTypes 是一个Object的可变数组，parameterTypes由Class<?>的可变数组 ，完整类名字符串和XC_MethodHook抽象类 组成。XC_MethodHook为可选参数，并且总在最后一个。XC_MethodHook在这里并无实际意义，Class<?>[] 为相应的构造函数的类型，通过一个例子简单说明，有一个T类，构造函数有三个参数，可以用以下几种方式获取：

***

``` java
public class T {
    String str;
    Context mContext;
    View mView;

    public T(String str, Context context, View view) {
        this.str = str;
        mContext = context;
        mView = view;
       
    }

}

//方式1：
Constructor constructor = XposedHelpers.findConstructorExact(clazz, String.class, Context.class, View.class);

//方式2：
Constructor constructor = XposedHelpers.findConstructorExact(T.class, String.class, "android.content.Context", View.class);

//方式3：（XC_MethodHook无实际意义）
Constructor constructor = XposedHelpers.findConstructorExact(T.class, String.class, "android.content.Context", View.class, new XC_MethodHook() {});
```

***

``` java
public static void setXXXField(Object obj, String fieldName, XXX value)
public static void setStaticXXXField(Class<?> clazz, String fieldName, XXX value)

public static Xxx getXxxField(Object obj, String fieldName)
public static Xxx getStaticXxxField(Class<?> clazzj, String fieldName)

```
设置或者获取Field的值，obj为实例，则为设置或者获取该成员变量的值

***


``` java
public static Object callMethod(Object obj, String methodName, Object... args)

public static Object callMethod(Object obj, String methodName, Class<?>[] parameterTypes, Object... args)

public static Object callStaticMethod(Class<?> clazz, String methodName, Object... args)

public static Object callStaticMethod(Class<?> clazz, String methodName, Class<?>[] parameterTypes, Object... args)
```
调用实例/静态Method，返回值为方法返回值

***


``` java
public static XC_MethodHook.Unhook findAndHookMethod(Class<?> clazz, String methodName, Object... parameterTypesAndCallback)

//通过className和classLoader获取Class<?> ，再调用上面的方法
public static XC_MethodHook.Unhook findAndHookMethod(String className, ClassLoader classLoader, String methodName, Object... parameterTypesAndCallback)
```
Hook方法的一个方法，其中parameterTypesAndCallback和findConstructorExact方法的parameterTypes类似，不过这里可变数组最后一个对象必须为XC_MethodHook对象或者其子类，前面的对象为参数的ClassType或者类字符串，在hook成功后，当调用hook的方法时，会在XC_MethodHook回调

``` java
public abstract class XC_MethodHook extends XCallback {
			@Override
			protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
				//方法调用前的回调
				super.beforeHookedMethod(param);
			}

			@Override
			protected void afterHookedMethod(MethodHookParam param) throws Throwable {
				//方法调用后的回调
				super.afterHookedMethod(param);
			}
		}
		
public abstract class XC_MethodReplacement extends XC_MethodHook{
			@Override
			protected Object replaceHookedMethod(MethodHookParam param) throws Throwable {
				//带返回值的方法执行时调用
				return null;
			}
		}
```
可以通过这两个class进行hook监听。


## 本节示例

git提交：[45c44ab4be96f012e7c4992bfdcc3bc2d3e458d7][1]

``` vim
git checkout 45c44ab
```


[1]: https://github.com/WrBug/XposedDemo/tree/45c44ab4be96f012e7c4992bfdcc3bc2d3e458d7