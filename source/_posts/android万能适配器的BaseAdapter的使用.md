---
title: android万能适配器的BaseAdapter的使用
categories:
- 文章
tags:
- Adapter
date: 2015-06-12 17:47:42
---

Android BaseAdapter(基础适配器）的用法，适配器的作用主要是用来给诸如(Spinner、ListView、GridView)来填充数据的。而(Spinner、
ListView、GridView)都有自己的适配器。
<!-- more -->
但是BaseAdapter对他们是通用的，首
先我们看一下API文档：[**baseAdapter**](/doc/reference/android/widget/BaseAdapter.html)

我们看到Android BaseAdapter已经实现了ListAdapter和SpinnerAdapter的接口，而GridView的适配器是实现了ListAdapter接口，只不过是二维的。所以说BaseAdapter对他们三者来说是通用的。

就是我们定义一个类(如：MyAdapter)而这个类继承BaseAdapter.因为它是implements了ListAdapter和SpinnerAdapter的接口，所以要实现里面的方法，代码如下(未作任何改动的）：
<div class="container"><div class="line number1 index0 alt2"></div><div class="line number25 index24 alt2"><pre class="brush:java;toolbar:false">private class MyAdapter extendsBaseAdapter {
    @Override
    public int getCount() {                   
        // TODO Auto-generated method stub
        return 0;
    }
 
    @Override
    public Object getItem(int arg0) {
        // TODO Auto-generated method stub
        return null;
    }
 
    @Override
    public long getItemId(int position) {
        // TODO Auto-generated method stub
        return 0;
    }
 
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        // TODO Auto-generated method stub
        return null;
    }
}</pre></div></div>