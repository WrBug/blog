---
title: 模仿QQ上线下线ImageView头像变灰
categories:
- 文章
tags: 
- QQ上线下线
date: 2015-06-22 21:18:08
---
<!-- more -->
<span style="font-size: 24px; color: rgb(255, 0, 0);">主要代码</span>
<pre class="brush:java;toolbar:false">ColorMatrix matrix = new ColorMatrix();
matrix.setSaturation(0);
ColorMatrixColorFilter filter = new ColorMatrixColorFilter(
    matrix);
imageView.setColorFilter(filter);</pre>

<span style="font-size: 24px; color: rgb(255, 0, 0);">DEMO工程代码：</span>

<span style="font-size: 18px;">MainActivity.java</span><span style="font-size: 24px;">
</span>
<pre class="brush:java;toolbar:false">public class MainActivity extends ActionBarActivity {
    ImageView imageView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        imageView = (ImageView) findViewById(R.id.imageView1);
        Button button = (Button) findViewById(R.id.button1);
        button.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View arg0) {
                // TODO Auto-generated method stub
                ColorMatrix matrix = new ColorMatrix();
                matrix.setSaturation(0);
                ColorMatrixColorFilter filter = new ColorMatrixColorFilter(
                        matrix);
                imageView.setColorFilter(filter);
            }
        });
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
}</pre>

<span style="font-size: 18px;">activity_main.xml</span>

<pre class="brush:xml;toolbar:false">&lt;RelativeLayout xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
    xmlns:tools=&quot;http://schemas.android.com/tools&quot;
    android:layout_width=&quot;match_parent&quot;
    android:layout_height=&quot;match_parent&quot;
    android:paddingBottom=&quot;@dimen/activity_vertical_margin&quot;
    android:paddingLeft=&quot;@dimen/activity_horizontal_margin&quot;
    android:paddingRight=&quot;@dimen/activity_horizontal_margin&quot;
    android:paddingTop=&quot;@dimen/activity_vertical_margin&quot;
    tools:context=&quot;com.example.demo.MainActivity&quot; &gt;
    &lt;Button
        android:id=&quot;@+id/button1&quot;
        android:layout_width=&quot;wrap_content&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:layout_alignParentBottom=&quot;true&quot;
        android:layout_alignParentLeft=&quot;true&quot;
        android:layout_alignParentRight=&quot;true&quot;
        android:text=&quot;变暗&quot; /&gt;
    &lt;ImageView
        android:id=&quot;@+id/imageView1&quot;
        android:layout_width=&quot;wrap_content&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:layout_above=&quot;@+id/button1&quot;
        android:layout_alignLeft=&quot;@+id/button1&quot;
        android:layout_alignParentTop=&quot;true&quot;
        android:layout_alignRight=&quot;@+id/button1&quot;
        android:src=&quot;@drawable/ic_launcher&quot; /&gt;
&lt;/RelativeLayout&gt;</pre>