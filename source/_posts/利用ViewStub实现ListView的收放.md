---
title: 利用ViewStub实现ListView的收放
categories:
- 文章
tags: 
- ViewStub
date: 2015-07-31 00:35:02
---

ViewStub经常用在ListView中，用来隐藏一些操作，使用起来也很简单，主要就是在ListView的Item中通过一个ViewStub来引用被隐藏的布局文件。监听用户点击Item，判断下当前是可见还是不可见，实时进行状态的转换即可。
<!-- more -->
效果图如下：

![](/upload/2015/07/201507311438274262700084.gif)

MainActivity.java: 
<pre class="brush:java;toolbar:false">public class MainActivity extends Activity {
    private ListView lvList;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        lvList = (ListView)findViewById(R.id.lv_list);
        List&lt;Map&lt;String, String&gt;&gt; data = new ArrayList&lt;Map&lt;String, String&gt;&gt;();
        Map&lt;String, String&gt; map;
        for(int i = 0; i &lt; 20; i++){
            
            map = new HashMap&lt;String, String&gt;();
            map.put(&quot;1234&quot;, &quot;1234&quot;);
            data.add(map);
        }
        
        MainAdapter mainAdapter = new MainAdapter(this, data);
        lvList.setAdapter(mainAdapter);
    }
}</pre>

MainAdapter.java:

自定义Adapter，在getView中实现我们的效果：
<pre class="brush:java;toolbar:false">public class MainAdapter extends BaseAdapter {
//    private Context context;
    private List&lt;Map&lt;String, String&gt;&gt; data;
    private LayoutInflater layoutInflater;
    public MainAdapter(Context context, List&lt;Map&lt;String, String&gt;&gt; data) {
//        this.context = context;
        this.data = data;
        layoutInflater = (LayoutInflater) context
                .getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        
    }
    class ViewHolder {
        RelativeLayout rlListItem;// 点击展开或收起ViewStub
        View vsOperations;// 点击后显示的更多的操作
        ImageButton ibCompelete;// 打钩按钮
        ImageButton ibImportant;// 感叹号按钮
        ImageButton ibNotify;// 提醒按钮
        ImageButton ibLove;// 爱心按钮
        ImageButton ibShare;// 分享按钮
    }
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        final ViewHolder viewHolder;
        if (convertView == null) {
            convertView = layoutInflater.inflate(R.layout.list_item_main_task,
                    null);
            viewHolder = new ViewHolder();
            viewHolder.rlListItem = (RelativeLayout) convertView
                    .findViewById(R.id.rl_list_item);
            viewHolder.vsOperations = (ViewStub) convertView
                    .findViewById(R.id.vs_detail_operations);
            convertView.setTag(viewHolder);
        } else {
            viewHolder = (ViewHolder) convertView.getTag();
            viewHolder.vsOperations.setVisibility(View.GONE);
        }
        viewHolder.rlListItem.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                if (viewHolder.vsOperations.getVisibility() == View.GONE) {
                    
                    if(viewHolder.vsOperations instanceof ViewStub){
                        //关键！
                        viewHolder.vsOperations = ((ViewStub)viewHolder.vsOperations).inflate();
                    }
                    viewHolder.vsOperations.setVisibility(View.VISIBLE);
                    
                } else {
                    viewHolder.vsOperations.setVisibility(View.GONE);
                }
            }
        });
        Log.e(&quot;111&quot;, &quot;getView&quot;);
        
        return convertView;
    }
    @Override
    public int getCount() {
        // TODO Auto-generated method stub
        return data.size();
    }
    @Override
    public Object getItem(int position) {
        // TODO Auto-generated method stub
        return data.get(position);
    }
    @Override
    public long getItemId(int position) {
        // TODO Auto-generated method stub
        return position;
    }
}</pre>

activity_main.xml:
<pre class="brush:xml;toolbar:false">&lt;RelativeLayout xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
    xmlns:tools=&quot;http://schemas.android.com/tools&quot;
    android:layout_width=&quot;match_parent&quot;
    android:layout_height=&quot;match_parent&quot;
    tools:context=&quot;.MainActivity&quot; &gt;
    &lt;ListView
        android:id=&quot;@+id/lv_list&quot;
        android:layout_width=&quot;match_parent&quot;
        android:layout_height=&quot;match_parent&quot;
         /&gt;
&lt;/RelativeLayout&gt;</pre>

list_item_main_task.xml: ListView中的每个Item，注意里面的ViewStub,通过它来引用一个布局文件，即隐藏的操作按钮。
<pre class="brush:xml;toolbar:false">&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;LinearLayout xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
    android:layout_width=&quot;wrap_content&quot;
    android:layout_height=&quot;wrap_content&quot;
    android:orientation=&quot;vertical&quot; &gt;
    &lt;!-- 每个ListItem除了ViewStub，都在这个标签里面 --&gt;
    &lt;RelativeLayout
        android:id=&quot;@+id/rl_list_item&quot;
        android:layout_width=&quot;wrap_content&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:background=&quot;@drawable/bg_list_item_task&quot;
        android:gravity=&quot;center&quot; &gt;
        &lt;!-- android:descendantFocusability=&quot;blocksDescendants&quot; 当ListView setOnItemClickListener点击没有效果的时候，加上这个 --&gt;
        &lt;!-- 任务的名称和超期时间 --&gt;
        &lt;LinearLayout
            android:layout_width=&quot;fill_parent&quot;
            android:layout_height=&quot;wrap_content&quot;
            android:layout_centerVertical=&quot;true&quot;
            android:gravity=&quot;center_vertical&quot;
            android:orientation=&quot;vertical&quot; &gt;
            &lt;TextView
                android:id=&quot;@+id/tv_task_name&quot;
                android:layout_width=&quot;wrap_content&quot;
                android:layout_height=&quot;wrap_content&quot;
                android:text=&quot;任务1&quot;
                android:textColor=&quot;#404040&quot;
                android:textSize=&quot;22dp&quot; /&gt;
            &lt;LinearLayout
                android:layout_width=&quot;wrap_content&quot;
                android:layout_height=&quot;wrap_content&quot;
                android:gravity=&quot;center_vertical&quot;
                android:orientation=&quot;horizontal&quot; &gt;
                &lt;TextView
                    android:id=&quot;@+id/tv_over_date&quot;
                    android:layout_width=&quot;wrap_content&quot;
                    android:layout_height=&quot;wrap_content&quot;
                    android:text=&quot;超期2天&quot;
                    android:textColor=&quot;#ff0000&quot;
                    android:textSize=&quot;15dp&quot; /&gt;
                &lt;TextView
                    android:id=&quot;@+id/tv_name&quot;
                    android:layout_width=&quot;wrap_content&quot;
                    android:layout_height=&quot;wrap_content&quot;
                    android:layout_marginLeft=&quot;5dip&quot;
                    android:text=&quot;张小三&quot;
                    android:textColor=&quot;#333333&quot;
                    android:textSize=&quot;15dp&quot; /&gt;
            &lt;/LinearLayout&gt;
        &lt;/LinearLayout&gt;
    &lt;/RelativeLayout&gt;
    &lt;ViewStub
        android:id=&quot;@+id/vs_detail_operations&quot;
        android:layout_width=&quot;wrap_content&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:layout=&quot;@layout/view_stub_tool_bar&quot; /&gt;
&lt;/LinearLayout&gt;</pre>

view_stub_tool_bar.xml: 被隐藏的操作按钮
<pre class="brush:xml;toolbar:false">&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;LinearLayout xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
    android:layout_width=&quot;wrap_content&quot;
    android:layout_height=&quot;wrap_content&quot;
    android:orientation=&quot;horizontal&quot;
    android:gravity=&quot;center_vertical&quot;
    android:paddingTop=&quot;8dip&quot;
    android:background=&quot;@drawable/bg_list_item_task_view_stub&quot; &gt;
    &lt;ImageButton
        android:id=&quot;@+id/btn_compelete&quot;
        android:layout_width=&quot;fill_parent&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:layout_weight=&quot;1&quot;
        android:minHeight=&quot;55dp&quot;
        android:background=&quot;@null&quot;
        android:src=&quot;@drawable/ico_complete_selector&quot; /&gt;
    &lt;ImageButton
        android:id=&quot;@+id/btn_important&quot;
        android:layout_width=&quot;fill_parent&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:layout_weight=&quot;1&quot;
        android:minHeight=&quot;55dp&quot;
        android:background=&quot;@null&quot;
        android:src=&quot;@drawable/ico_important_selector&quot; /&gt;
    &lt;ImageButton
        android:id=&quot;@+id/btn_&quot;
        android:layout_width=&quot;fill_parent&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:layout_weight=&quot;1&quot;
        android:minHeight=&quot;55dp&quot;
        android:background=&quot;@null&quot;
        android:src=&quot;@drawable/ico_notify_selector&quot; /&gt;
    &lt;ImageButton
        android:id=&quot;@+id/btn_&quot;
        android:layout_width=&quot;fill_parent&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:layout_weight=&quot;1&quot;
        android:minHeight=&quot;55dp&quot;
        android:background=&quot;@null&quot;
        android:src=&quot;@drawable/ico_love_selector&quot; /&gt;
    &lt;ImageButton
        android:id=&quot;@+id/btn_&quot;
        android:layout_width=&quot;fill_parent&quot;
        android:layout_height=&quot;wrap_content&quot;
        android:layout_weight=&quot;1&quot;
        android:minHeight=&quot;55dp&quot;
        android:background=&quot;@null&quot;
        android:src=&quot;@drawable/ico_share_selector&quot; /&gt;
&lt;/LinearLayout&gt;</pre>

使用ViewStub的好处是，它并没有实例化这个View对象，而是在用户点击的时候才进行实例化，这样可以提高效率。特别是当你的listItem比较复杂的时候，效果很明显。