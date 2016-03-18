---
title: android Adapter优化之终极版
categories:
- 文章
tags:
- Adapter
date: 2015-08-25 14:09:09
---

移动开发中个人认为最重要的就是应用的用户体验度,其中最重要的就是流畅度,而Android的Adapter优化就是很重要的一个方面,下面的代码就是一个Adapter的优化,当然从网上学习了很多大神写的代码,贴出来分享,大家共同进步,有什么好的建议可以留言评论
<!-- more -->
<pre class="brush:java;toolbar:false">import android.content.Context;
import android.util.SparseArray;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import java.util.ArrayList;
public abstract class BaseArrayListAdapter&lt;T&gt; extends BaseAdapter {
    protected ArrayList&lt;T&gt; data;
    @Override
    public int getCount() {
        // TODO Auto-generated method stub
        return (data == null) ? 0 : data.size();
    }
    @Override
    public Object getItem(int position) {
        // TODO Auto-generated method stub
        return position;
    }
    @Override
    public long getItemId(int position) {
        // TODO Auto-generated method stub
        return position;
    }
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        // TODO Auto-generated method stub
        return getViewHolder(convertView, parent, position).getConvertView();
    }
    public abstract ViewHolder getViewHolder(View convertView,
        ViewGroup parent, int position);
    static class ViewHolder {
        private final SparseArray&lt;View&gt; views;
        private View convertView;
        private ViewHolder(Context mContext, View convertView) {
            this.views = new SparseArray&lt;View&gt;();
            this.convertView = convertView;
            convertView.setTag(this);
        }
        public static ViewHolder get(Context mContext, View convertView,
            ViewGroup parent, int resId) {
            if (convertView == null) {
                LayoutInflater factory = (LayoutInflater) mContext.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
                convertView = factory.inflate(resId, parent, false); //
                return new ViewHolder(mContext, convertView);
            }
            return (ViewHolder) convertView.getTag();
        }
        @SuppressWarnings(&quot;unchecked&quot;)
        public &lt;T extends View&gt; T findViewById(int resourceId) {
            View view = views.get(resourceId);
            if (view == null) {
                view = convertView.findViewById(resourceId);
                views.put(resourceId, view);
            }
            return (T) view;
        }
        public View getConvertView() {
            return convertView;
        }
        public void setConvertView(View convertView) {
            this.convertView = convertView;
        }
    }
}</pre>