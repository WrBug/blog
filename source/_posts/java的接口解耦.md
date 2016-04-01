---
title: java的接口解耦
categories:
- 杂七杂八
tags: 
- 解耦
date: 2015-10-22 14:30:49
---

<span style="color: rgb(51, 51, 51); font-family: Arial; font-size: 18px; line-height: 26px; background-color: rgb(255, 255, 255);">     学过java的人都知道，java是单继承的，也就是说一个class只能继承一个类。</span>
<!-- more -->
<span style="color: rgb(51, 51, 51); font-family: Arial; font-size: 18px; line-height: 26px; background-color: rgb(255, 255, 255);">       例如我们想制作一台有播放器的手机，那么我们先得制作一个播放器吧，再把播放器放进手机里。在java会怎么实现呢？如果使用继承，我们会先创建一个播放器类，播放器类里面含有播放歌曲功能（方法），创建一个手机类继承播放器类，重写播放器的播歌功能（不重写的话，会直接使用播放器自己定制的播放功能），这样，我们就可以使用手机的播歌功能了。</span>
<span style="color: rgb(51, 51, 51); font-family: Arial; font-size: 18px; line-height: 26px; background-color: rgb(255, 255, 255);">       现在，我们想制作一台既有播歌功能，又有收音机功能的手机，那么我们该怎么办？难道我们又要让继承了播放器的手机再继承收音机？但是java是单继承的，行不通，这时，接口应运而生！</span>

<span style="color: rgb(51, 51, 51); font-family: Arial; font-size: 18px; line-height: 26px; background-color: rgb(255, 255, 255);">      接口，乍一看就是包含几个方法的一个东西，它里面不包含具体实现的代码，只包含方法的返回类型，名称，参数列表，它代表的是一个功能的集合，只要实现了这个接口的类，他就具有了这些功能。</span>
<span style="color: rgb(51, 51, 51); font-family: Arial; font-size: 18px; line-height: 26px; background-color: rgb(255, 255, 255);">       回到之前说的既有播歌又有收音机功能的手机，现在我们不把播放器和收音机封装成类了，我们把它们封装成接口（接口就是功能的集合），创建手机类，实现播放器和收音机接口，这样看起来，是不是有点像多继承？这违背了java的单继承原则吗？</span>

<span style="color: rgb(51, 51, 51); font-family: Arial; font-size: 18px; line-height: 26px; background-color: rgb(255, 255, 255);">       其实没有，有些书里面提到的多重继承指的是多个实现接口。继承（extends），是一种 is-a 关系的，所谓is-a关系，就是类似于“手机是播放器”或者“手机是收音机”这样说法，但明显，我们不能说“手机既是播放器又是收音机”，那么“他究竟是播放器还是收音机？”，这时大家就会可能这样发问了，这就是java是单继承的原因。实现（implement），是一种hava-a关系的，所谓have-a就是具有“某一项功能“的意思，我们这时候会说“手机既有播放器功能，又有收音机功能”，这样的表达该明白了吧！让手机再添加其他功能，只要再让他实现那些功能接口就好了。</span>

<span style="color: rgb(51, 51, 51); font-family: Arial; font-size: 18px; line-height: 26px; background-color: rgb(255, 255, 255);">        好像说了那么多还没说到正题~哈哈，其实举前面的例子我是想说明一个问题：只要一个方法操作的是类而非接口，那么你只能使用这个类及其之类。如果你想要将这个方法应用于不在此继承结构中的某个类，那么你就触霉头了。接口可以在很大程度上放宽这种限制，因此，他使我们可以编写可复用性更好的代码。——引用《thinking in java》的某一些话。</span>
<span style="color: rgb(51, 51, 51); font-family: Arial; font-size: 18px; line-height: 26px; background-color: rgb(255, 255, 255);">         </span>
<span style="color: rgb(51, 51, 51); font-family: Arial; font-size: 18px; line-height: 26px; background-color: rgb(255, 255, 255);">        举例子：我需要一个闹钟，放在我床边，每天叫我起床。但是我家里没闹钟，只有一台有闹钟功能的手机和一台有闹钟功能的洗衣机。我需要的只是闹钟功能，我管他是什么，只要他能让我起床就好了。如果某一天我连手机都丢了，我能把洗衣机放在我床边叫我起床吗？当然可以，因为洗衣机实现了闹钟功能。所以，我们经常会这么做：把“闹钟”这个功能（而不是具体的某一项事物，如手机或者洗衣机）放在床边，如果我们想听洗衣机的闹钟声就摆洗衣机，如果想听手机的闹钟声就摆手机。</span>
<span style="color: rgb(51, 51, 51); font-family: Arial; font-size: 18px; line-height: 26px; background-color: rgb(255, 255, 255);">         从上面的例子，我们传递的不是某个具体的对象，而是一个抽象的“闹钟功能”的概念，至于实际上传递的是什么参数，要看具体情况（取决于我想听哪一种闹钟声）。实际上，我们只关心“具有闹钟功能”这件事，我们不关心它是由谁实现的和怎样实现的，这就做到了“请求”和“实现”分离开来，这就是接口的解耦！</span>