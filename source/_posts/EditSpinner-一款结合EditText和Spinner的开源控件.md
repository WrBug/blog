---
title: EditSpinner 一款结合EditText和Spinner的开源控件
tags: []
date: 2016-02-28 18:05:09
---
<!-- more -->
<span style="font-size: 20px;">效果演示：</span>

![201602281456654040118978.gif](http://www.mandroid.cn/zb_users/upload/2016/02/201602281456654040118978.gif "201602281456654040118978.gif")

项目地址：[https://github.com/wangtao2132/EditSpinner](https://github.com/wangtao2132/EditSpinner)

<span style="font-size: 20px;">项目介绍：</span>

EditSpinner是一款结合EditText和Spinner的控件，可以自行输入和下拉选择，类似于AutoCompleteTextView

使用说明：
<pre class="brush:java;toolbar:false">&lt;cn.mandroid.widget.editspinner.EditSpinner
&nbsp;&nbsp;&nbsp;&nbsp;android:id=&quot;@+id/editSpinner1&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width=&quot;match_parent&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height=&quot;wrap_content&quot;
&nbsp;&nbsp;&nbsp;&nbsp;app:Background=&quot;@drawable/bg_view_frame&quot;
&nbsp;&nbsp;&nbsp;&nbsp;app:hint=&quot;EditSpinner&nbsp;Test&quot;
&nbsp;&nbsp;&nbsp;&nbsp;app:rightImage=&quot;@drawable/ic_expand_more_black&quot;&nbsp;/&gt;</pre><pre class="brush:java;toolbar:false">spinner1&nbsp;=&nbsp;(EditSpinner)&nbsp;findViewById(R.id.editSpinner1);
//设置控件右侧图片资源，默认资源为R.drawable.ic_expand_more_black
spinner1.setRightImageResource(R.drawable.ic_expand_more_black);
//设置控件Hint
spinner1.setHint(&quot;EditSpinner&quot;);
//设置下拉列表数据（List&lt;String&gt;）
spinner2.setItemData(list);</pre>