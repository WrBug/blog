---
title: RadioButton自定义样式底部导航
tags: [test]
date: 2015-06-17 00:47:59
---

<span style="font-size: 24px;">先上效果：</span>

<span style="font-size: 20px;">![QQ截图20150617010130.png](http://www.mandroid.cn/zb_users/upload/2015/06/201506171434474172281858.png "201506171434474172281858.png")</span>
<!-- more -->
<span style="font-size: 24px;">布局文件<span style="color: rgb(255, 0, 0);">_main.xml_</span>：</span>
<span style="font-size: 20px;"><pre class="brush:java;toolbar:false">&lt;RelativeLayout&nbsp;xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
&nbsp;&nbsp;&nbsp;&nbsp;xmlns:tools=&quot;http://schemas.android.com/tools&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width=&quot;match_parent&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height=&quot;match_parent&quot;
&nbsp;&nbsp;&nbsp;&nbsp;tools:context=&quot;.MainActivity&quot;&nbsp;&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;TextView
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width=&quot;wrap_content&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height=&quot;wrap_content&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_centerHorizontal=&quot;true&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_centerVertical=&quot;true&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:text=&quot;@string/hello_world&quot;&nbsp;/&gt;
&lt;!—设置底部导航栏&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;LinearLayout
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width=&quot;fill_parent&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height=&quot;wrap_content&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_alignParentBottom=&quot;true&quot;&nbsp;&gt;
&lt;!—引用底部导航栏的布局文件&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;include
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:id=&quot;@+id/footbar_layout_ly&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;layout=&quot;@layout/footbar_layout&quot;&nbsp;/&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;/LinearLayout&gt;
&lt;/RelativeLayout&gt;</pre></span>

<span style="font-size: 20px;"></span>

<span style="font-size: 24px;">底部导航栏布局文件<span style="color: rgb(255, 0, 0);">_footbar_layout.xml_</span>：</span>
<span style="font-size: 20px;"><pre class="brush:java;toolbar:false">&lt;?xml&nbsp;version=&quot;1.0&quot;&nbsp;encoding=&quot;utf-8&quot;?&gt;
&lt;LinearLayout&nbsp;xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width=&quot;fill_parent&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height=&quot;60dp&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:background=&quot;#ffffff&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:orientation=&quot;horizontal&quot;&nbsp;&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;RadioGroup
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width=&quot;fill_parent&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height=&quot;match_parent&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:orientation=&quot;horizontal&quot;&nbsp;&gt;
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;RadioButton
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--radiobutton样式，在文章下面有说明。下同--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;style=&quot;@style/radio_button_style&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--导航栏图标，下同--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:drawableTop=&quot;@drawable/bottom&quot;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--导航文字，下同--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:text=&quot;文字&quot;&nbsp;/&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;RadioButton
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;style=&quot;@style/radio_button_style&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:drawableTop=&quot;@drawable/bottom&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:text=&quot;文字&quot;&nbsp;/&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;RadioButton
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;style=&quot;@style/radio_button_style&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:drawableTop=&quot;@drawable/bottom&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:text=&quot;文字&quot;&nbsp;/&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;/RadioGroup&gt;
&lt;/LinearLayout&gt;</pre></span>

<span style="font-size: 24px;">在styles.xml中添加<span style="color: rgb(255, 0, 0);">radio_button_style</span>名称的布局:</span>
<span style="font-size: 20px;"><pre class="brush:java;toolbar:false">&lt;resources&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;style&nbsp;name=&quot;navigation_bottom_radio&quot;&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;内部组件的排列&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;name=&quot;android:gravity&quot;&gt;center_horizontal&lt;/item&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;背景样式&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;name=&quot;android:background&quot;&gt;@drawable/style_navigation_radio&lt;/item&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;宽度&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;name=&quot;android:layout_width&quot;&gt;fill_parent&lt;/item&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;高度&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;name=&quot;android:layout_height&quot;&gt;wrap_content&lt;/item&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;设置RadioButton的原来图片为空&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;name=&quot;android:button&quot;&gt;@null&lt;/item&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;与其他组件宽度占相同比重&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;name=&quot;android:layout_weight&quot;&gt;1.0&lt;/item&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;底部的空隙&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;name=&quot;android:paddingBottom&quot;&gt;2.0dip&lt;/item&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;顶部的空隙&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;name=&quot;android:paddingTop&quot;&gt;2.0dip&lt;/item&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;文字的大小&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;name=&quot;android:textSize&quot;&gt;11dip&lt;/item&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;文字的颜色&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;name=&quot;android:textColor&quot;&gt;@color/white&lt;/item&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;/style&gt;
&lt;/resources&gt;</pre></span>

<span style="font-size: 24px;">在res\drawable目录下添加每个Radio的背景的样式<span style="color: rgb(255, 0, 0);">_style_navigation_radio.xml_</span></span>
<span style="font-size: 20px;"><pre class="brush:xml;toolbar:false">&nbsp;&nbsp;&nbsp;&lt;?xml&nbsp;version=&quot;1.0&quot;&nbsp;encoding=&quot;utf-8&quot;?&gt;
&lt;selector&nbsp;xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;选中&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;android:drawable=&quot;@drawable/选中时的背景图&quot;&nbsp;android:state_checked=&quot;true&quot;/&gt;
&lt;/selector&gt;</pre></span>

&nbsp;