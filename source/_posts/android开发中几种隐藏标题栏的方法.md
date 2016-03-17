---
title: android开发中几种隐藏标题栏的方法
tags: []
date: 2015-06-21 19:07:37
---

<div class="content-list-text">

<span style="font-size: 24px;"></span>

<span style="font-size: 24px;">1\. <span style="font-size: 24px; color: rgb(255, 0, 0);"><span style="font-size: 24px;">推荐</span>！</span><span style="font-size: 24px; color: rgb(255, 0, 0);">（因为现在工程都默认的为AppTheme）</span>
</span>

在value/styles.xml里面添加自定义属性
<pre class="brush:xml;toolbar:false">&lt;resources&nbsp;xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;Application&nbsp;theme.&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;style&nbsp;name=&quot;AppTheme&quot;&nbsp;parent=&quot;AppBaseTheme&quot;&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;name=&quot;android:windowNoTitle&quot;&gt;true&lt;/item&gt;
&lt;/resources&gt;</pre></div><div class="content-list-media"><div class="content-list-image clearfix">

<span class="exp-album-enter-mask"></span>

<span style="font-size: 24px;">2.</span>
<pre class="brush:java;toolbar:false">public&nbsp;class&nbsp;MainActivity&nbsp;extends&nbsp;Activity{
&nbsp;&nbsp;&nbsp;&nbsp;@Override
&nbsp;&nbsp;&nbsp;&nbsp;protected&nbsp;void&nbsp;onCreate(Bundle&nbsp;savedInstanceState){
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;super.onCreate(savedInstanceState);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;隐藏标题栏
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;requestWindowFeature(Window.FEATURE_NO_TITLE);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;隐藏状态栏
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WindowManager.LayoutParams.FLAG_FULLSCREEN);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//一定要放在setContentView()之前！
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;setContentView(R.layout.activity_main);
&nbsp;&nbsp;&nbsp;&nbsp;}
}</pre>

<span style="font-size: 24px;">3.</span>

<pre class="brush:xml;toolbar:false">&lt;!--&nbsp;Application&nbsp;theme.&nbsp;--&gt;
&lt;style&nbsp;name=&quot;AppTheme&quot;&nbsp;parent=&quot;AppBaseTheme&quot;&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;All&nbsp;customizations&nbsp;that&nbsp;are&nbsp;NOT&nbsp;specific&nbsp;to&nbsp;a&nbsp;particular&nbsp;API-level&nbsp;can&nbsp;go&nbsp;here.&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;隐藏状态栏&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;name=&quot;android:windowFullscreen&quot;&gt;true&lt;/item&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;!--&nbsp;隐藏标题栏&nbsp;--&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;item&nbsp;name=&quot;android:windowNoTitle&quot;&gt;true&lt;/item&gt;
&lt;/style&gt;</pre>

<span class="exp-album-enter-mask"></span><span style="font-size: 24px;">4.</span>

</div></div><pre class="brush:xml;toolbar:false">&lt;!--&nbsp;同时隐藏状态栏和标题栏&nbsp;&nbsp;--&gt;
&lt;activity
&nbsp;&nbsp;&nbsp;&nbsp;android:name=&quot;com.ysj.demo.MainActivity&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:theme=&quot;@android:style/Theme.NoTitleBar.Fullscreen&quot;
&nbsp;&nbsp;&nbsp;&nbsp;android:label=&quot;@string/app_name&quot;&nbsp;&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;intent-filter&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;action&nbsp;android:name=&quot;android.intent.action.MAIN&quot;&nbsp;/&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;category&nbsp;android:name=&quot;android.intent.category.LAUNCHER&quot;&nbsp;/&gt;
&nbsp;&nbsp;&nbsp;&nbsp;&lt;/intent-filter&gt;
&lt;/activity&gt;</pre>

<span style="font-size: 24px;">5.</span>打开项目文件AndroidManifest.xml ，打开Application选择TAB页，在页面下方的Application Nodes中点选择相应的类,&nbsp;&nbsp; 配置右侧的Theme属性。
<div class="content-list-media"><div class="content-list-image clearfix">![d058ccbf6c81800ab49240c9b33533fa838b4786.jpg](http://www.mandroid.cn/zb_users/upload/2015/06/201506211434885529850695.jpg "201506211434885529850695.jpg")<span class="exp-album-enter-mask"></span></div></div><div class="content-list-text">

在弹出选择框中点选&quot;system Resources&quot;，选择Theme.NoTitleBar项目，然后重新打开页面就行了。
</div>

![5366d0160924ab18767128f037fae6cd7a890b96.jpg](http://www.mandroid.cn/zb_users/upload/2015/06/201506211434885550436342.jpg "201506211434885550436342.jpg")