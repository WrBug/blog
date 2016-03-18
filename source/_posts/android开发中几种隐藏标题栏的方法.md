---
title: android开发中几种隐藏标题栏的方法
categories:
- 文章
date: 2015-06-21 19:07:37
---
<!-- more -->
<div class="content-list-text">

<span style="font-size: 24px;"></span>

<span style="font-size: 24px;">1\. <span style="font-size: 24px; color: rgb(255, 0, 0);"><span style="font-size: 24px;">推荐</span>！</span><span style="font-size: 24px; color: rgb(255, 0, 0);">（因为现在工程都默认的为AppTheme）</span>
</span>

## 在value/styles.xml里面添加自定义属性
<pre class="brush:xml;toolbar:false">&lt;resources xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;&gt;
    &lt;!-- Application theme. --&gt;
    &lt;style name=&quot;AppTheme&quot; parent=&quot;AppBaseTheme&quot;&gt;
       &lt;item name=&quot;android:windowNoTitle&quot;&gt;true&lt;/item&gt;
&lt;/resources&gt;</pre></div><div class="content-list-media"><div class="content-list-image clearfix">

<span class="exp-album-enter-mask"></span>

## 2.
<pre class="brush:java;toolbar:false">public class MainActivity extends Activity{
    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        // 隐藏标题栏
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        // 隐藏状态栏
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
        WindowManager.LayoutParams.FLAG_FULLSCREEN);
       //一定要放在setContentView()之前！
        setContentView(R.layout.activity_main);
    }
}</pre>

## 3.
<pre class="brush:xml;toolbar:false">&lt;!-- Application theme. --&gt;
&lt;style name=&quot;AppTheme&quot; parent=&quot;AppBaseTheme&quot;&gt;
    &lt;!-- All customizations that are NOT specific to a particular API-level can go here. --&gt;
    &lt;!-- 隐藏状态栏 --&gt;
    &lt;item name=&quot;android:windowFullscreen&quot;&gt;true&lt;/item&gt;
    &lt;!-- 隐藏标题栏 --&gt;
    &lt;item name=&quot;android:windowNoTitle&quot;&gt;true&lt;/item&gt;
&lt;/style&gt;</pre>

<span class="exp-album-enter-mask"></span><span style="font-size: 24px;">4.</span>

</div></div><pre class="brush:xml;toolbar:false">&lt;!-- 同时隐藏状态栏和标题栏  --&gt;
&lt;activity
    android:name=&quot;com.ysj.demo.MainActivity&quot;
    android:theme=&quot;@android:style/Theme.NoTitleBar.Fullscreen&quot;
    android:label=&quot;@string/app_name&quot; &gt;
    &lt;intent-filter&gt;
        &lt;action android:name=&quot;android.intent.action.MAIN&quot; /&gt;
        &lt;category android:name=&quot;android.intent.category.LAUNCHER&quot; /&gt;
    &lt;/intent-filter&gt;
&lt;/activity&gt;</pre>
## 4.
打开项目文件AndroidManifest.xml ，打开Application选择TAB页，在页面下方的Application Nodes中点选择相应的类,   配置右侧的Theme属性。
<div class="content-list-media"><div class="content-list-image clearfix">![d058ccbf6c81800ab49240c9b33533fa838b4786.jpg](/upload/2015/06/201506211434885529850695.jpg "201506211434885529850695.jpg")<span class="exp-album-enter-mask"></span></div></div><div class="content-list-text">

在弹出选择框中点选&quot;system Resources&quot;，选择Theme.NoTitleBar项目，然后重新打开页面就行了。
</div>

![5366d0160924ab18767128f037fae6cd7a890b96.jpg](/upload/2015/06/201506211434885550436342.jpg "201506211434885550436342.jpg")