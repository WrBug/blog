---
title: Android Adapter优化(二)之Adapter对不同布局的支持
categories:
- 杂七杂八
tags:
- Adapter
date: 2015-08-25 14:12:03
---

在Android开发过程中,用到的控件最多的就是ListView了，相信大家在做应用的过程中展示数据许多时候都需要在一个ListView上展示不同的布局吧,这个Android的Adapter机制本身就是支持的代码如下:
<!-- more -->
## 1,adapter的内容:
<pre class="brush:java;toolbar:false">import java.util.ArrayList;
import android.content.Context;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import com.betterandroid.adapter.base.BaseArrayListAdapter;
import com.betterandroid.bitmap.ajaxbitmap.AjaxBitmap;
public class MyAdapter extends BaseArrayListAdapter&lt;MyBean&gt; {
        private Context mContext;
        private FinalBitmap ajaxBitmap;
        public MyAdapter(Context mContext, ArrayList&lt;MyBean&gt; list) {
                super();
                this.mContext = mContext;
                this.data = list;
                ajaxBitmap = FinalBitmap .create(mContext);
        }
        @Override
        public int getViewTypeCount() {
                // TODO Auto-generated method stub
                return 3;
        }
        
        @Override
        public int getItemViewType(int position) {
                // TODO Auto-generated method stub
                if(data.get(position).getType() == 0) {
                        return 0;
                }
                if(data.get(position).getType() == 1) {
                        return 1;
                }
                return 2;
        }
        
        
        @Override
        public ViewHolder getViewHolder(
                        View convertView, ViewGroup parent, int position) {
                // TODO Auto-generated method stub
                ViewHolder mViewHolder = null;
                int type = getItemViewType(position);
                switch (type) {
                case 0:
                        mViewHolder = ViewHolder.get(mContext, convertView, parent, R.layout.list_item);
                        TextView text = mViewHolder.findViewById(R.id.text);
                        text.setText(data.get(position).getContent());
                        break;
                case 1:
                        mViewHolder = ViewHolder.get(mContext, convertView, parent, R.layout.list_item_two);
                        ImageView imageview = mViewHolder.findViewById(R.id.imageview);
                        ajaxBitmap.display(imageview, data.get(position).getContent());
                        break;
                case 2:
                        mViewHolder = ViewHolder.get(mContext, convertView, parent, R.layout.list_item_three);
                        ImageView image = mViewHolder.findViewById(R.id.image);
                        ImageView image1 = mViewHolder.findViewById(R.id.image1);
                        ajaxBitmap.display(image, data.get(position).getContent());
                        ajaxBitmap.display(image1, data.get(position).getContent());
                        break;
                default:
                        break;
                }
                return mViewHolder;
        }</pre>

## 2，activity内容:
<pre class="brush:java;toolbar:false">import java.util.ArrayList;
import android.app.Activity;
import android.os.Bundle;
import android.widget.ListView;
public class MainActivity extends Activity {
        private ListView listview;
        @Override
        protected void onCreate(Bundle savedInstanceState) {
                super.onCreate(savedInstanceState);
                setContentView(R.layout.activity_main);
                listview = (ListView) this.findViewById(R.id.listview);
                MyAdapter adapter = new MyAdapter(getApplicationContext(), initData());
                listview.setAdapter(adapter);
        }
        
        private ArrayList&lt;MyBean&gt; initData() {
                // TODO Auto-generated method stub
                ArrayList&lt;MyBean&gt; list = new ArrayList&lt;MyBean&gt;();
                for (int i = 0; i &lt; 80; i++) {
                        MyBean bean;
                        if(i%3==0) {
                                bean = new MyBean(0, &quot;text&quot;+i);
                        } else if(i%3 == 1){
                                bean = new MyBean(1, IMAGE_DEMO[i%14]);
                        } else {
                                bean = new MyBean(2, IMAGE_DEMO[i%14]);
                        }
                        list.add(bean);
                }
                return list;
        }
        
        /**
         * 测试图片
         */
        public String[] IMAGE_DEMO = {
                        &quot;http://g.hiphotos.baidu.com/image/pic/item/0bd162d9f2d3572cb707d6dd8813632763d0c3ce.jpg&quot;,
                        &quot;http://b.hiphotos.baidu.com/image/pic/item/bba1cd11728b4710604224c1c1cec3fdfc03234a.jpg&quot;,
                        &quot;http://g.hiphotos.baidu.com/image/pic/item/3bf33a87e950352a18846f095143fbf2b3118bce.jpg&quot;,
                        &quot;http://h.hiphotos.baidu.com/image/pic/item/b3fb43166d224f4a97ffc6120bf790529822d149.jpg&quot;,
                        &quot;http://b.hiphotos.baidu.com/image/pic/item/e4dde71190ef76c6aeb24e2a9f16fdfaaf51674a.jpg&quot;,
                        &quot;http://c.hiphotos.baidu.com/image/pic/item/4a36acaf2edda3cc9ecc193f03e93901213f9281.jpg&quot;,
                        &quot;http://h.hiphotos.baidu.com/image/pic/item/241f95cad1c8a786beb13e066509c93d70cf501a.jpg&quot;,
                        &quot;http://e.hiphotos.baidu.com/image/pic/item/e824b899a9014c08f25c9da4087b02087bf4f448.jpg&quot;,
                        &quot;http://h.hiphotos.baidu.com/image/pic/item/d788d43f8794a4c23243522a0cf41bd5ad6e394a.jpg&quot;,
                        &quot;http://b.hiphotos.baidu.com/image/pic/item/6609c93d70cf3bc7d6ad8dead300baa1cd112a02.jpg&quot;,
                        &quot;http://h.hiphotos.baidu.com/image/pic/item/b219ebc4b74543a905b7baca1c178a82b9011403.jpg&quot;,
                        &quot;http://d.hiphotos.baidu.com/image/pic/item/c8ea15ce36d3d53955944fc53887e950352ab00f.jpg&quot;,
                        &quot;http://e.hiphotos.baidu.com/image/pic/item/241f95cad1c8a7860504930c6509c93d70cf5082.jpg&quot;,
                        &quot;http://h.hiphotos.baidu.com/image/pic/item/4e4a20a4462309f77ff6d318700e0cf3d7cad61b.jpg&quot; };
}</pre>

## 3，XMl布局：
activity_main.xml
<pre class="brush:xml;toolbar:false">&lt;RelativeLayout xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
    xmlns:tools=&quot;http://schemas.android.com/tools&quot;
    android:layout_width=&quot;match_parent&quot;
    android:layout_height=&quot;match_parent&quot; &gt;
    &lt;ListView
        android:id=&quot;@+id/listview&quot;
        android:layout_width=&quot;match_parent&quot;
        android:layout_height=&quot;match_parent&quot; /&gt;
&lt;/RelativeLayout&gt;</pre>

list_item.xml
<pre class="brush:xml;toolbar:false">&lt;RelativeLayout xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
    xmlns:tools=&quot;http://schemas.android.com/tools&quot;
    android:layout_width=&quot;match_parent&quot;
    android:layout_height=&quot;match_parent&quot;
    android:layout_gravity=&quot;center&quot;
    android:gravity=&quot;center&quot; &gt;
    &lt;TextView
        android:id=&quot;@+id/text&quot;
        android:layout_width=&quot;match_parent&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:gravity=&quot;center&quot;
        android:text=&quot;aaa&quot; /&gt;
&lt;/RelativeLayout&gt;</pre>

list_item_two.xml
<pre class="brush:xml;toolbar:false">&lt;RelativeLayout xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
    xmlns:tools=&quot;http://schemas.android.com/tools&quot;
    android:layout_width=&quot;match_parent&quot;
    android:layout_height=&quot;match_parent&quot;
    android:layout_gravity=&quot;center&quot;
    android:gravity=&quot;center&quot; &gt;
    &lt;ImageView
        android:id=&quot;@+id/imageview&quot;
        android:layout_width=&quot;match_parent&quot;
        android:layout_height=&quot;match_parent&quot; /&gt;
&lt;/RelativeLayout&gt;</pre>

list_item_three.xml
<pre class="brush:xml;toolbar:false">&lt;LinearLayout xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
    xmlns:tools=&quot;http://schemas.android.com/tools&quot;
    android:layout_width=&quot;match_parent&quot;
    android:layout_height=&quot;match_parent&quot;
    android:layout_gravity=&quot;center&quot;
    android:orientation=&quot;horizontal&quot;
    android:gravity=&quot;center&quot; &gt;
    &lt;ImageView
        android:id=&quot;@+id/image&quot;
        android:layout_width=&quot;wrap_content&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:layout_weight=&quot;1&quot; /&gt;
    
    &lt;ImageView
        android:id=&quot;@+id/image1&quot;
        android:layout_width=&quot;wrap_content&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:layout_weight=&quot;1&quot; /&gt;
&lt;/LinearLayout&gt;</pre>