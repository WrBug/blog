---
title: android退出所有的activity
tags: []
date: 2015-06-22 21:35:41
---
<!-- more -->
<span style="font-size: 20px;"><span style="color: rgb(68, 68, 68); background-color: rgb(255, 255, 255);">Android经典完美退出方法，使用单例模式创建一个Activity管理对象，该对象中有一个Activity容器（具体实现自己处理，使用LinkedList等）专门负责存储新开启的每一个Activity，并且容易理解、易于操作，非常不错！</span>
 <span style="color: rgb(68, 68, 68); background-color: rgb(255, 255, 255); font-size: 14px;">AppUtils类（储存每一个Activity，并实现关闭所有Activity的操作）</span></span>

<pre class="brush:java;toolbar:false">package com.cpic.jscx.android.utils; 
 import android.app.Activity; 
 import android.app.Application; 
 import java.util.LinkedList; 
 import java.util.List; 
 public class AppUtils extends Application{ 
     private List&lt;Activity&gt; activityList = new LinkedList&lt;Activity&gt;(); 
     private static AppUtils instance; 
             private AppUtils() 
             { 
             } 
              //单例模式中获取唯一的app实例 
              public static AppUtils getInstance() 
              { 
                             if(null == instance) 
                           { 
                              instance = new AppUtils(); 
                           } 
                  return instance;             
              } 
              //添加Activity到容器中 
              public void addActivity(Activity activity) 
              { 
                             activityList.add(activity); 
              } 
              //遍历所有Activity并finish 
              public void exit() 
              { 
                           for(Activity activity:activityList) 
                          { 
                            activity.finish(); 
                          } 
                            System.exit(0); 
             } 
 }</pre>

activity实现：

<pre class="brush:java;toolbar:false">public class MainActivity extends ActionBarActivity {
    private  AppUtils appUtils;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        appUtils=AppUtils.getInstance();
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
    @Override
    public void onDestroy() {
        appUtils.exit();
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