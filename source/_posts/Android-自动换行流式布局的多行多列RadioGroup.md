---
title: Android 自动换行流式布局的多行多列RadioGroup
categories:
- 文章
date: 2015-07-12 23:05:56
---
<!-- more -->
![04155106-9f598b9f5ed34195ab7482d69729fb26.png](/upload/2015/07/201507121436713650204443.png "201507121436713650204443.png")

<pre class="brush:java;toolbar:false">import android.content.Context;
import android.util.AttributeSet;
import android.view.View;
import android.widget.RadioGroup;
/**
 * 流式布局的RadioGroup
 */
public class FlowRadioGroup extends RadioGroup {
    
    public FlowRadioGroup(Context context) {
        super(context);
    }
    public FlowRadioGroup(Context context, AttributeSet attrs) {
        super(context, attrs);
    }
    @Override
    protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
        int maxWidth = MeasureSpec.getSize(widthMeasureSpec);
        int childCount = getChildCount();
        int x = 0;
        int y = 0;
        int row = 0;
        for (int index = 0; index &lt; childCount; index++) {
            final View child = getChildAt(index);
            if (child.getVisibility() != View.GONE) {
                child.measure(MeasureSpec.UNSPECIFIED, MeasureSpec.UNSPECIFIED);
                // 此处增加onlayout中的换行判断，用于计算所需的高度
                int width = child.getMeasuredWidth();
                int height = child.getMeasuredHeight();
                x += width;
                y = row * height + height;
                if (x &gt; maxWidth) {
                    x = width;
                    row++;
                    y = row * height + height;
                }
            }
        }
        // 设置容器所需的宽度和高度
        setMeasuredDimension(maxWidth, y);
    }
    @Override
    protected void onLayout(boolean changed, int l, int t, int r, int b) {
        final int childCount = getChildCount();
        int maxWidth = r - l;
        int x = 0;
        int y = 0;
        int row = 0;
        for (int i = 0; i &lt; childCount; i++) {
            final View child = this.getChildAt(i);
            if (child.getVisibility() != View.GONE) {
                int width = child.getMeasuredWidth();
                int height = child.getMeasuredHeight();
                x += width;
                y = row * height + height;
                if (x &gt; maxWidth) {
                    x = width;
                    row++;
                    y = row * height + height;
                }
                child.layout(x - width, y - height, x, y);
            }
        }
    }
}</pre>