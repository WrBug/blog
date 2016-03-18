---
title: RadioButton自定义样式底部导航
categories:
- 文章
tags: 
- 底部导航
date: 2015-06-17 00:47:59
---

<span style="font-size: 24px;">先上效果：</span>

<span style="font-size: 20px;">![QQ截图20150617010130.png](/upload/2015/06/201506171434474172281858.png "201506171434474172281858.png")</span>
<!-- more -->
<span style="font-size: 24px;">布局文件<span style="color: rgb(255, 0, 0);">_main.xml_</span>：</span>
<span style="font-size: 20px;"><pre class="brush:java;toolbar:false">&lt;RelativeLayout xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
    xmlns:tools=&quot;http://schemas.android.com/tools&quot;
    android:layout_width=&quot;match_parent&quot;
    android:layout_height=&quot;match_parent&quot;
    tools:context=&quot;.MainActivity&quot; &gt;
    &lt;TextView
        android:layout_width=&quot;wrap_content&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:layout_centerHorizontal=&quot;true&quot;
        android:layout_centerVertical=&quot;true&quot;
        android:text=&quot;@string/hello_world&quot; /&gt;
&lt;!—设置底部导航栏 --&gt;
    &lt;LinearLayout
        android:layout_width=&quot;fill_parent&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:layout_alignParentBottom=&quot;true&quot; &gt;
&lt;!—引用底部导航栏的布局文件 --&gt;
        &lt;include
            android:id=&quot;@+id/footbar_layout_ly&quot;
            layout=&quot;@layout/footbar_layout&quot; /&gt;
    &lt;/LinearLayout&gt;
&lt;/RelativeLayout&gt;</pre></span>

<span style="font-size: 20px;"></span>

<span style="font-size: 24px;">底部导航栏布局文件<span style="color: rgb(255, 0, 0);">_footbar_layout.xml_</span>：</span>
<span style="font-size: 20px;"><pre class="brush:java;toolbar:false">&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;LinearLayout xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
    android:layout_width=&quot;fill_parent&quot;
    android:layout_height=&quot;60dp&quot;
    android:background=&quot;#ffffff&quot;
    android:orientation=&quot;horizontal&quot; &gt;
    &lt;RadioGroup
        android:layout_width=&quot;fill_parent&quot;
        android:layout_height=&quot;match_parent&quot;
        android:orientation=&quot;horizontal&quot; &gt;
 
        &lt;RadioButton
             &lt;!--radiobutton样式，在文章下面有说明。下同--&gt;
            style=&quot;@style/radio_button_style&quot;
            &lt;!--导航栏图标，下同--&gt;
            android:drawableTop=&quot;@drawable/bottom&quot;  
            &lt;!--导航文字，下同--&gt;
            android:text=&quot;文字&quot; /&gt;
        &lt;RadioButton
            style=&quot;@style/radio_button_style&quot;
            android:drawableTop=&quot;@drawable/bottom&quot;
            android:text=&quot;文字&quot; /&gt;
        &lt;RadioButton
            style=&quot;@style/radio_button_style&quot;
            android:drawableTop=&quot;@drawable/bottom&quot;
            android:text=&quot;文字&quot; /&gt;
    &lt;/RadioGroup&gt;
&lt;/LinearLayout&gt;</pre></span>

<span style="font-size: 24px;">在styles.xml中添加<span style="color: rgb(255, 0, 0);">radio_button_style</span>名称的布局:</span>
<span style="font-size: 20px;"><pre class="brush:java;toolbar:false">&lt;resources&gt;
    &lt;style name=&quot;navigation_bottom_radio&quot;&gt;
        &lt;!-- 内部组件的排列 --&gt;
        &lt;item name=&quot;android:gravity&quot;&gt;center_horizontal&lt;/item&gt;
        &lt;!-- 背景样式 --&gt;
        &lt;item name=&quot;android:background&quot;&gt;@drawable/style_navigation_radio&lt;/item&gt;
        &lt;!-- 宽度 --&gt;
        &lt;item name=&quot;android:layout_width&quot;&gt;fill_parent&lt;/item&gt;
        &lt;!-- 高度 --&gt;
        &lt;item name=&quot;android:layout_height&quot;&gt;wrap_content&lt;/item&gt;
        &lt;!-- 设置RadioButton的原来图片为空 --&gt;
        &lt;item name=&quot;android:button&quot;&gt;@null&lt;/item&gt;
        &lt;!-- 与其他组件宽度占相同比重 --&gt;
        &lt;item name=&quot;android:layout_weight&quot;&gt;1.0&lt;/item&gt;
        &lt;!-- 底部的空隙 --&gt;
        &lt;item name=&quot;android:paddingBottom&quot;&gt;2.0dip&lt;/item&gt;
        &lt;!-- 顶部的空隙 --&gt;
        &lt;item name=&quot;android:paddingTop&quot;&gt;2.0dip&lt;/item&gt;
        &lt;!-- 文字的大小 --&gt;
        &lt;item name=&quot;android:textSize&quot;&gt;11dip&lt;/item&gt;
        &lt;!-- 文字的颜色 --&gt;
        &lt;item name=&quot;android:textColor&quot;&gt;@color/white&lt;/item&gt;
    &lt;/style&gt;
&lt;/resources&gt;</pre></span>

<span style="font-size: 24px;">在res\drawable目录下添加每个Radio的背景的样式<span style="color: rgb(255, 0, 0);">_style_navigation_radio.xml_</span></span>
<span style="font-size: 20px;"><pre class="brush:xml;toolbar:false">   &lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;selector xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;&gt;
    &lt;!-- 选中 --&gt;
    &lt;item android:drawable=&quot;@drawable/选中时的背景图&quot; android:state_checked=&quot;true&quot;/&gt;
&lt;/selector&gt;</pre></span>

 