---
title: 模仿QQ上线下线ImageView头像变灰
tags: []
date: 2015-06-22 21:18:08
---

<span style="font-size: 24px; color: rgb(255, 0, 0);">效果图</span>

!(http://www.mandroid.cn/zb_users/upload/2015/06/201506221434979262141789.png "201506221434979262141789.png")
<!-- more -->
<span style="font-size: 24px; color: rgb(255, 0, 0);">主要代码</span>
<pre class="brush:java;toolbar:false">ColorMatrix&nbsp;matrix&nbsp;=&nbsp;new&nbsp;ColorMatrix();
matrix.setSaturation(0);
ColorMatrixColorFilter&nbsp;filter&nbsp;=&nbsp;new&nbsp;ColorMatrixColorFilter(
&nbsp;&nbsp;&nbsp;&nbsp;matrix);
imageView.setColorFilter(filter);</pre>

<span style="font-size: 24px; color: rgb(255, 0, 0);">DEMO工程代码：</span>

<span style="font-size: 18px;">MainActivity.java</span><span style="font-size: 24px;">
</span>
<pre class="brush:java;toolbar:false">public&nbsp;class&nbsp;MainActivity&nbsp;extends&nbsp;ActionBarActivity&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;ImageView&nbsp;imageView;
&nbsp;&nbsp;&nbsp;&nbsp;@Override
&nbsp;&nbsp;&nbsp;&nbsp;protected&nbsp;void&nbsp;onCreate(Bundle&nbsp;savedInstanceState)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;super.onCreate(savedInstanceState);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;setContentView(R.layout.activity_main);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;imageView&nbsp;=&nbsp;(ImageView)&nbsp;findViewById(R.id.imageView1);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Button&nbsp;button&nbsp;=&nbsp;(Button)&nbsp;findViewById(R.id.button1);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;button.setOnClickListener(new&nbsp;OnClickListener()&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;@Override
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public&nbsp;void&nbsp;onClick(View&nbsp;arg0)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;TODO&nbsp;Auto-generated&nbsp;method&nbsp;stub
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ColorMatrix&nbsp;matrix&nbsp;=&nbsp;new&nbsp;ColorMatrix();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;matrix.setSaturation(0);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ColorMatrixColorFilter&nbsp;filter&nbsp;=&nbsp;new&nbsp;ColorMatrixColorFilter(
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;matrix);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;imageView.setColorFilter(filter);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;});
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;@Override
&nbsp;&nbsp;&nbsp;&nbsp;public&nbsp;boolean&nbsp;onCreateOptionsMenu(Menu&nbsp;menu)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Inflate&nbsp;the&nbsp;menu;&nbsp;this&nbsp;adds&nbsp;items&nbsp;to&nbsp;the&nbsp;action&nbsp;bar&nbsp;if&nbsp;it&nbsp;is&nbsp;present.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;getMenuInflater().inflate(R.menu.main,&nbsp;menu);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;true;
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;@Override
&nbsp;&nbsp;&nbsp;&nbsp;public&nbsp;boolean&nbsp;onOptionsItemSelected(MenuItem&nbsp;item)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;Handle&nbsp;action&nbsp;bar&nbsp;item&nbsp;clicks&nbsp;here.&nbsp;The&nbsp;action&nbsp;bar&nbsp;will
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;automatically&nbsp;handle&nbsp;clicks&nbsp;on&nbsp;the&nbsp;Home/Up&nbsp;button,&nbsp;so&nbsp;long
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;as&nbsp;you&nbsp;specify&nbsp;a&nbsp;parent&nbsp;activity&nbsp;in&nbsp;AndroidManifest.xml.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;int&nbsp;id&nbsp;=&nbsp;item.getItemId();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;(id&nbsp;==&nbsp;R.id.action_settings)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;true;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;super.onOptionsItemSelected(item);
&nbsp;&nbsp;&nbsp;&nbsp;}
}</pre>

<span style="font-size: 18px;">activity_main.xml</span>

<pre class="brush:xml;toolbar:false">&lt;RelativeLayout&nbsp;xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
&nbsp;&nbsp;&nbsp;&nbsp;xmlns:tools=&quot;http://schemas.android.com/tools&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width=&quot;match_parent&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height=&quot;match_parent&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:paddingBottom=&quot;@dimen/activity_vertical_margin&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:paddingLeft=&quot;@dimen/activity_horizontal_margin&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:paddingRight=&quot;@dimen/activity_horizontal_margin&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:paddingTop=&quot;@dimen/activity_vertical_margin&quot;
&nbsp;&nbsp;&nbsp;&nbsp;tools:context=&quot;com.example.demo.MainActivity&quot;&nbsp;&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;Button
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:id=&quot;@+id/button1&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width=&quot;wrap_content&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height=&quot;wrap_content&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_alignParentBottom=&quot;true&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_alignParentLeft=&quot;true&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_alignParentRight=&quot;true&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:text=&quot;变暗&quot;&nbsp;/&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;ImageView
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:id=&quot;@+id/imageView1&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_width=&quot;wrap_content&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_height=&quot;wrap_content&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_above=&quot;@+id/button1&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_alignLeft=&quot;@+id/button1&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_alignParentTop=&quot;true&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:layout_alignRight=&quot;@+id/button1&quot;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;android:src=&quot;@drawable/ic_launcher&quot;&nbsp;/&gt;
&lt;/RelativeLayout&gt;</pre>