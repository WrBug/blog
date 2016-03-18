---
title: ViewHolder的简洁写法
categories:
- 文章
tags: 
- ViewHolder
- ListView
date: 2015-06-24 15:57:04
---
<!-- more -->
<pre class="brush:java;toolbar:false">public class ViewHolder {
    // I added a generic return type to reduce the casting noise in client code
    @SuppressWarnings(&quot;unchecked&quot;)
    public static &lt;T extends View&gt; T get(View view, int id) {
        SparseArray&lt;View&gt; viewHolder = (SparseArray&lt;View&gt;) view.getTag();
        if (viewHolder == null) {
            viewHolder = new SparseArray&lt;View&gt;();
            view.setTag(viewHolder);
        }
        View childView = viewHolder.get(id);
        if (childView == null) {
            childView = view.findViewById(id);
            viewHolder.put(id, childView);
        }
        return (T) childView;
    }
}</pre>

<span style="color:#333333"><span style="font-family:Arial">ViewHolder这么写（只提供一个静态方法，其实可以加一个私有构造函数防止外部实例化），代码很简单，看过就明白了</span></span>
<pre class="brush:java;toolbar:false">public View getView(int position, View convertView, ViewGroup parent)
 {
    if (convertView == null) {
        convertView = LayoutInflater.from(context)
          .inflate(R.layout.banana_phone, parent, false);
    }
    ImageView bananaView = ViewHolder.get(convertView, R.id.banana);
    TextView phoneView = ViewHolder.get(convertView, R.id.phone);
    BananaPhone bananaPhone = getItem(position);
    phoneView.setText(bananaPhone.getPhone());
    bananaView.setImageResource(bananaPhone.getBanana());
    return convertView;
}</pre>