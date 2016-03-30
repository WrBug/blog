---
title: Android涉及到的设计模式
categories:
- 文章
tags:
- 设计模式
date: 2015-06-29 10:43:37
---

## 1、适配器模式：
ListView或GridView的Adapter

简介：不同的数据提供者使用一个适配器来向一个相同的客户提供服务。
<!-- more -->
 

## 2、建造者模式：
AlertDialog.Builder

简介：可以分步地构造每一部分。

 

## 3、命令模式：
Handler.post后Handler.handleMessage

简介：把请求封装成一个对象发送出去，方便定制、排队、取消。

 

## 4、享元模式：
Message.obtainMessage通过重用Message对象来避免大量的Message对象被频繁的创建和销毁。

简介：运用共享技术有效地支持大量细粒度的对象。

 

## 5、迭代器模式：
如通过Hashtable.elements方法可以得到一个Enumeration，然后通过这个Enumeration访问Hashtable中的数据，而不用关心Hashtable中的数据存放方式。

简介：提供一个方法顺序访问数据集合中的所有数据而又不暴露对象的内部表示。

 

## 6、备忘录模式：
Activity的onSaveInstanceState和onRestoreInstanceState就是通过Bundle这种序列化的数据结构来存储Activity的状态，至于其中存储的数据结构，这两个方法不用关心

简介：不需要了解对象的内部结构的情况下备份对象的状态，方便以后恢复。

 

## 7、观察者模式：
我们可以通过BaseAdapter.registerDataSetObserver和
BaseAdapter.unregisterDataSetObserver两方法来向BaseAdater注册、注销一个
DataSetObserver。这个过程中，DataSetObserver就是一个观察者，它一旦发现BaseAdapter内部数据有变量，就会通
过回调方法DataSetObserver.onChanged和DataSetObserver.onInvalidated来通知
DataSetObserver的实现类。事件通知也是观察者模式

简介：一个对象发生改变时，所有信赖于它的对象自动做相应改变。

 

## 8、原型模式：
比如我们需要一张Bitmap的几种不同格式：ARGB_8888、RGB_565、ARGB_4444、ALAPHA_8等。那我
们就可以先创建一个ARGB_8888的Bitmap作为原型，在它的基础上，通过调用Bitmap.copy(Config)来创建出其它几种格式的
Bitmap。另外一个例子就是Java中所有对象都有的一个名字叫clone的方法，已经原型模式的代名词了

简介：在系统中要创建大量的对象，这些对象之间具有几乎完全相同的功能，只是在细节上有一点儿差别。

 

## 9、代理模式：
类似于ios开发的delegate委托模式，所有的AIDL都一个代理模式的例子。假设一个Activity 
A去绑定一个Service 
S，那么A调用S中的每一个方法其实都是通过系统的Binder机制的中转，然后调用S中的对应方法来做到的。Binder机制就起到了代理的作用。

简介：为其他对象提供一种代理以控制对这个对象的访问。

 

## 10、状态模式：
View.onVisibilityChanged方法，就是提供了一个状态模式的实现，允许在View的visibility发生改变时，引发执行onVisibilityChanged方法中的动作。

<span style="color:#000000">简介：状态发生改变时，行为改变。</span>

 

## 11、策略模式：

举例：Java.util.List就是定义了一个增（add）、删（remove）、改（set）、查（indexOf）策略，至于实现这个策略
的ArrayList、LinkedList等类，只是在具体实现时采用了不同的算法。但因为它们策略一样，不考虑速度的情况下，使用时完全可以互相替换
使用。

简介：定义了一系列封装了算法、行为的对象，他们可以相互替换。

 

## 12、调解者模式

简介：一个对象的某个操作需要调用N个对象的M个方法来完成时，把这些调用过程封装起来，就成了一个调解者

举例：如Resource.getDrawable方法的实现逻辑是这样的：创建一个缓存来存放所有已经加载过的，如果getDrawable中传
入的id所对应的Drawable以前没有被加载过，那么它就会根据id所对应的资源类型，分别调用XML解析器生成，或者通过读取包中的图片资源文件来
创建Drawable。

而Resource.getDrawable把涉及到多个对象、多个逻辑的操作封装成一个方法，就实现了一个调解者的角色。

 

## 13、抽象工厂模式

DAO与Service的使用
</div>