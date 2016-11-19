---
title: 解决AndroidonClick与onTouch冲突
categories:
- 杂七杂八
tags: android,事件分发,view解读,反射
grammar_cjkRuby: true
date: 2016-11-19 23:55:30
---

在进行android开发时难免同时会用到onClick和onTouch事件，比如要实现view有click事件，并且通过onTouch实现了跟随手指而移动，在移动完成后不进行人和事情。如果直接使用，在移动完成松手以后也会出现click事件，主要在于android的事件分发机制原因。本文将通过反射机制来实现
<!-- more -->
## View事件的分发机制
本文只对会用到的事件的响应顺序做一些简单的介绍，更多的分析请查找其他资料
为了便于理解，直接通过代码来进行分析,创建一个activity，摆放一个button，button实现三个listener事件（setOnClickListener,setOnLongClickListener,setOnTouchListener），代码如下：

``` java
        Button button = (Button) findViewById(R.id.button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.i("mandroid.cn", "button被点击");
            }
        });
        button.setOnLongClickListener(new View.OnLongClickListener() {
            @Override
            public boolean onLongClick(View view) {
                Log.i("mandroid.cn", "button被长按");
                return false;
            }
        });
        button.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent motionEvent) {
                switch (motionEvent.getAction()) {
                    case MotionEvent.ACTION_DOWN: {
                        Log.i("mandroid.cn", "button按下");
                        break;
                    }
                    case MotionEvent.ACTION_MOVE: {
                        Log.i("mandroid.cn", "button移动");
                        break;
                    }
                    case MotionEvent.ACTION_UP: {
                        Log.i("mandroid.cn", "button松开");
                        break;
                    }
                }
				//返回true不响应click事件
                return true;
            }
        });
```
运行后按下button，查看打印的log如下

``` stylus
11-20 00:28:11.005 27548-27548/com.wrbug.myapplication I/mandroid.cn: button按下
11-20 00:28:11.017 27548-27548/com.wrbug.myapplication I/mandroid.cn: button移动
11-20 00:28:11.034 27548-27548/com.wrbug.myapplication I/mandroid.cn: button移动
11-20 00:28:11.042 27548-27548/com.wrbug.myapplication I/mandroid.cn: button移动
11-20 00:28:11.051 27548-27548/com.wrbug.myapplication I/mandroid.cn: button移动
11-20 00:28:11.059 27548-27548/com.wrbug.myapplication I/mandroid.cn: button移动
11-20 00:28:11.066 27548-27548/com.wrbug.myapplication I/mandroid.cn: button移动
11-20 00:28:11.067 27548-27548/com.wrbug.myapplication I/mandroid.cn: button松开
```
可以发现并未响应onClick和onLongClick事件，是由于在onTouch里面返回为true时，就不会往其他地方分发，将返回改为false再次运行：

``` stylus
11-20 00:47:27.020 21781-21781/com.wrbug.myapplication I/mandroid.cn: button按下
11-20 00:47:27.052 21781-21781/com.wrbug.myapplication I/mandroid.cn: button移动
11-20 00:47:27.069 21781-21781/com.wrbug.myapplication I/mandroid.cn: button移动
11-20 00:47:27.070 21781-21781/com.wrbug.myapplication I/mandroid.cn: button松开
11-20 00:47:27.070 21781-21781/com.wrbug.myapplication V/AudioManager: playSoundEffect   effectType: 0
11-20 00:47:27.070 21781-21781/com.wrbug.myapplication V/AudioManager: querySoundEffectsEnabled...
11-20 00:47:27.070 21781-21781/com.wrbug.myapplication I/mandroid.cn: button被点击
```
改为false的时候。在移动完成时都会响应click事件，目前我们就是要实现检测到view在移动后，不执行click和longclick操作，没有移动则执行。

## 实现
为了方便，只以onClick的方式来讲解。通过查看View的源码，View的listener都存在一个静态内部类里面
view源码查看地址：[http://android.mandroid.cn/java/android/view/View.java][1]
``` java
 static class ListenerInfo {
        /**
         * Listener used to dispatch focus change events.
         * This field should be made private, so it is hidden from the SDK.
         * {@hide}
         */
        protected OnFocusChangeListener mOnFocusChangeListener;

        /**
         * Listeners for layout change events.
         */
        private ArrayList<OnLayoutChangeListener> mOnLayoutChangeListeners;

        protected OnScrollChangeListener mOnScrollChangeListener;

        /**
         * Listeners for attach events.
         */
        private CopyOnWriteArrayList<OnAttachStateChangeListener> mOnAttachStateChangeListeners;

        /**
         * Listener used to dispatch click events.
         * This field should be made private, so it is hidden from the SDK.
         * {@hide}
         */
        public OnClickListener mOnClickListener;

        /**
         * Listener used to dispatch long click events.
         * This field should be made private, so it is hidden from the SDK.
         * {@hide}
         */
        protected OnLongClickListener mOnLongClickListener;

        /**
         * Listener used to dispatch context click events. This field should be made private, so it
         * is hidden from the SDK.
         * {@hide}
         */
        protected OnContextClickListener mOnContextClickListener;

        /**
         * Listener used to build the context menu.
         * This field should be made private, so it is hidden from the SDK.
         * {@hide}
         */
        protected OnCreateContextMenuListener mOnCreateContextMenuListener;

        private OnKeyListener mOnKeyListener;

        private OnTouchListener mOnTouchListener;

        private OnHoverListener mOnHoverListener;

        private OnGenericMotionListener mOnGenericMotionListener;

        private OnDragListener mOnDragListener;

        private OnSystemUiVisibilityChangeListener mOnSystemUiVisibilityChangeListener;

        OnApplyWindowInsetsListener mOnApplyWindowInsetsListener;
    }

    ListenerInfo mListenerInfo;
```
通过反射获取mListenerInfo实例，再获取mListenerInfo里面的mOnClickListener，最后调用mOnClickListener.onClick()方法即可，修改后的onTouch代码如下
 

``` java
    button.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View view, MotionEvent motionEvent) {
                switch (motionEvent.getAction()) {
                    case MotionEvent.ACTION_DOWN: {
                        Log.i("mandroid.cn", "button按下");
                        //记录按下时的位置
                        x = motionEvent.getRawX();
                        y = motionEvent.getRawY();
                        break;
                    }
                    case MotionEvent.ACTION_MOVE: {
                        Log.i("mandroid.cn", "button移动");
                        break;
                    }
                    case MotionEvent.ACTION_UP: {
                        //检测移动的距离，如果很微小可以认为是点击事件
                        if (Math.abs(motionEvent.getRawX() - x) < 10 && Math.abs(motionEvent.getRawY() - y) < 10) {
                            try {
                                Field field = View.class.getDeclaredField("mListenerInfo");
                                field.setAccessible(true);
                                Object object = field.get(view);
                                field = object.getClass().getDeclaredField("mOnClickListener");
                                field.setAccessible(true);
                                object = field.get(object);
                                if (object != null && object instanceof View.OnClickListener) {
                                    ((View.OnClickListener) object).onClick(view);
                                }
                            } catch (Exception e) {

                            }
                        } else {
                            Log.i("mandroid.cn", "button已移动");
                        }
                        break;
                    }
                }
                return true;
            }
        });
```
log如下，也达到我们要求

``` stylus
//第一次点击
11-20 01:28:51.189 32174-32174/com.wrbug.myapplication I/mandroid.cn: button按下
11-20 01:28:52.057 32174-32174/com.wrbug.myapplication I/mandroid.cn: button被点击
//第二次点击
11-20 01:28:53.335 32174-32174/com.wrbug.myapplication I/mandroid.cn: button按下
11-20 01:28:54.055 32174-32174/com.wrbug.myapplication I/mandroid.cn: button被点击
//移动
11-20 01:28:55.238 32174-32174/com.wrbug.myapplication I/mandroid.cn: button按下
11-20 01:28:55.269 32174-32174/com.wrbug.myapplication I/mandroid.cn: button移动
11-20 01:28:55.278 32174-32174/com.wrbug.myapplication I/mandroid.cn: button移动
11-20 01:28:55.285 32174-32174/com.wrbug.myapplication I/mandroid.cn: button移动
11-20 01:28:55.294 32174-32174/com.wrbug.myapplication I/mandroid.cn: button移动
11-20 01:28:55.301 32174-32174/com.wrbug.myapplication I/mandroid.cn: button移动
11-20 01:28:55.302 32174-32174/com.wrbug.myapplication I/mandroid.cn: button已移动
```
## 应用到的项目 MoveableLayout
正在开发一款开源的控件，功能是一个layout里面的控件开源自由移动，互不影响，不交叉重叠，使用到了上述的方法，也欢迎大家star和提出建议，目前只实现了移动，近期会实现其他功能，参考地址：[https://github.com/WrBug/MoveableLayout][2]


  [1]: http://android.mandroid.cn/java/android/view/View.java
  [2]: https://github.com/WrBug/MoveableLayout