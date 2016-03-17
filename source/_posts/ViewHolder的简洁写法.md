---
title: ViewHolder的简洁写法
tags: []
date: 2015-06-24 15:57:04
---
<!-- more -->
<pre class="brush:java;toolbar:false">public&nbsp;class&nbsp;ViewHolder&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;//&nbsp;I&nbsp;added&nbsp;a&nbsp;generic&nbsp;return&nbsp;type&nbsp;to&nbsp;reduce&nbsp;the&nbsp;casting&nbsp;noise&nbsp;in&nbsp;client&nbsp;code
&nbsp;&nbsp;&nbsp;&nbsp;@SuppressWarnings(&quot;unchecked&quot;)
&nbsp;&nbsp;&nbsp;&nbsp;public&nbsp;static&nbsp;&lt;T&nbsp;extends&nbsp;View&gt;&nbsp;T&nbsp;get(View&nbsp;view,&nbsp;int&nbsp;id)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SparseArray&lt;View&gt;&nbsp;viewHolder&nbsp;=&nbsp;(SparseArray&lt;View&gt;)&nbsp;view.getTag();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;(viewHolder&nbsp;==&nbsp;null)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;viewHolder&nbsp;=&nbsp;new&nbsp;SparseArray&lt;View&gt;();
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;view.setTag(viewHolder);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;View&nbsp;childView&nbsp;=&nbsp;viewHolder.get(id);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;(childView&nbsp;==&nbsp;null)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;childView&nbsp;=&nbsp;view.findViewById(id);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;viewHolder.put(id,&nbsp;childView);
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;(T)&nbsp;childView;
&nbsp;&nbsp;&nbsp;&nbsp;}
}</pre>

<span style="color:#333333"><span style="font-family:Arial">ViewHolder这么写（只提供一个静态方法，其实可以加一个私有构造函数防止外部实例化），代码很简单，看过就明白了</span></span>
<pre class="brush:java;toolbar:false">public&nbsp;View&nbsp;getView(int&nbsp;position,&nbsp;View&nbsp;convertView,&nbsp;ViewGroup&nbsp;parent)
&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;(convertView&nbsp;==&nbsp;null)&nbsp;{
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;convertView&nbsp;=&nbsp;LayoutInflater.from(context)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.inflate(R.layout.banana_phone,&nbsp;parent,&nbsp;false);
&nbsp;&nbsp;&nbsp;&nbsp;}
&nbsp;&nbsp;&nbsp;&nbsp;ImageView&nbsp;bananaView&nbsp;=&nbsp;ViewHolder.get(convertView,&nbsp;R.id.banana);
&nbsp;&nbsp;&nbsp;&nbsp;TextView&nbsp;phoneView&nbsp;=&nbsp;ViewHolder.get(convertView,&nbsp;R.id.phone);
&nbsp;&nbsp;&nbsp;&nbsp;BananaPhone&nbsp;bananaPhone&nbsp;=&nbsp;getItem(position);
&nbsp;&nbsp;&nbsp;&nbsp;phoneView.setText(bananaPhone.getPhone());
&nbsp;&nbsp;&nbsp;&nbsp;bananaView.setImageResource(bananaPhone.getBanana());
&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;convertView;
}</pre>