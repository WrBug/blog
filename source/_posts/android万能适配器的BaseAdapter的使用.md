---
title: android万能适配器的BaseAdapter的使用
tags: []
date: 2015-06-12 17:47:42
---

Android BaseAdapter(基础适配器）的用法，适配器的作用主要是用来给诸如(Spinner、ListView、GridView)来填充数据的。而(Spinner、
ListView、GridView)都有自己的适配器。但是BaseAdapter对他们是通用的，首
先我们看一下API文档：[**baseAdapter**](/doc/reference/android/widget/BaseAdapter.html)

我们看到Android BaseAdapter已经实现了ListAdapter和SpinnerAdapter的接口，而GridView的适配器是实现了ListAdapter接口，只不过是二维的。所以说BaseAdapter对他们三者来说是通用的。

就是我们定义一个类(如：MyAdapter)而这个类继承BaseAdapter.因为它是implements了ListAdapter和SpinnerAdapter的接口，所以要实现里面的方法，代码如下(未作任何改动的）：
<div class="container"><div class="line number1 index0 alt2"></div><div class="line number25 index24 alt2"><pre class="brush:java;toolbar:false">private&nbsp;class&nbsp;MyAdapter&nbsp;extendsBaseAdapter&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;@Override
&nbsp;&nbsp;&nbsp;&nbsp;public&nbsp;int&nbsp;getCount()&nbsp;{&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;TODO&nbsp;Auto-generated&nbsp;method&nbsp;stub
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;0;
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;@Override
&nbsp;&nbsp;&nbsp;&nbsp;public&nbsp;Object&nbsp;getItem(int&nbsp;arg0)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;TODO&nbsp;Auto-generated&nbsp;method&nbsp;stub
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;null;
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;@Override
&nbsp;&nbsp;&nbsp;&nbsp;public&nbsp;long&nbsp;getItemId(int&nbsp;position)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;TODO&nbsp;Auto-generated&nbsp;method&nbsp;stub
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;0;
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;@Override
&nbsp;&nbsp;&nbsp;&nbsp;public&nbsp;View&nbsp;getView(int&nbsp;position,&nbsp;View&nbsp;convertView,&nbsp;ViewGroup&nbsp;parent)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;TODO&nbsp;Auto-generated&nbsp;method&nbsp;stub
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;null;
&nbsp;&nbsp;&nbsp;&nbsp;}
}</pre></div></div>