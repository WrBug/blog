---
title: Adroid zxing 二维码3.1集成（源码无删减）
tags: []
date: 2015-07-12 23:09:48
---

# Adroid zxing 二维码3.1集成

**文章转自：[http://my.oschina.net/gluoyer/blog/315947](http://my.oschina.net/gluoyer/blog/315947)**

_引子：最近项目中用到二维码，找到了最新的3.1版本_<span style="color: rgb(255, 0, 0); font-size: 20px;"> </span>[<span style="color: rgb(255, 0, 0); font-size: 20px;">zxing-GitHub</span>](https://github.com/zxing/zxing/)_，进行了集成、调整，同时笔记以备忘。_

_<span style="color:#9b00d3">求点击：博客访问9.9k+了，距离初步期望1w很近了。   一个多月的封闭开发也终于结束了，成都也雨后天晴出太阳。</span>_

_<span style="color:#9b00d3">    特此版本去掉了下载时需要积分的情况</span>_
<!-- more -->
实现效果：

    ![19115112_23fw.png](/upload/2015/07/201507131436788417101357.png "201507131436788417101357.png")

    相关博文很多，生成jar包，简化代码。度娘一下就有了。 感觉需要必要笔记，是发现：

*   以1.6版本居多，据说3.1对4x支持更好些。

*   简化后，对扩展比较麻烦。

*   修改竖屏后，修改的地方找起来比较麻烦。

### 未使用简化版本，直接引用zxing源码

    由于网上的简化版本，对功能扩展比较麻烦，因此，直接将zxing放到了工程目录下的extras/zxing下，只在项目中加入了目录，复制、修改了必要的文件，其他均引用源码文件

![19115113_8oXJ.jpg](/upload/2015/07/201507131436788453805554.jpg "201507131436788453805554.jpg")

### 修改竖屏后所需调整

    集成过程中，发现网文提到的修改竖屏，还是有点分散的，找起还是有点麻烦。故在<span style="color:#0000ff">CameraConfigurationManager</span>加了一个标识方法：<span style="color:#0000ff">isPortrait()</span>，返回<span style="color:#ff0000">true</span>

    例如，<span style="color:#0000ff">DecodeHandler.java</span>的<span style="color:#0000ff">decode</span>方法中需要调整，如下条件实现：

![19115114_4eQr.jpg](/upload/2015/07/201507131436788496442797.jpg "201507131436788496442797.jpg")

其他需要修改的地方，也如此使用<span style="color:#0000ff">isPortrait()</span>条件，所以，只需要看下<span style="color:#0000ff">isPortrait()</span>的<span style="color:#ccb400">Call Hierarchy</span>，就比较清晰得看到所需修改。

同时，返回<span style="color:#ff0000">false</span>，就可以恢复到源码处理。

### 绘制扫描框

    根据项目需求，需要重新绘制扫描框框，主要在<span style="color:#0000ff">ViewfinderView.java</span>实现绘制方法，同样条件控制，<span style="color:#0000ff">drawScanFrame</span>局部如下：

![19115116_xCkn.jpg](/upload/2015/07/201507131436788506598227.jpg "201507131436788506598227.jpg")

### 灯光的设置

    根据源码中，音量键对灯光的开关，添加了新接口，支持标题右上角对灯光的控制：

<span style="color:#0000ff">CameraManager.java</span>中：

![19115116_gKwu.jpg](/upload/2015/07/201507131436788519124077.jpg "201507131436788519124077.jpg")

以及<span style="color:#0000ff">CameraConfigurationManager.java</span>中：

![19115117_ue4m.jpg](/upload/2015/07/201507131436788593429629.jpg "201507131436788593429629.jpg")

在Activity中进行必要的调用处理即可。

### <span style="color:#0000ff">QrCaptureActivity</span> 中扫描成功的处理

   根据实际需求，扫描成功后，跳转并将数据传递给新页面，因此，只在<span style="color:#0000ff">handleDecode</span>方法中，

![19115119_Ehb6.jpg](/upload/2015/07/201507131436788571117265.jpg "201507131436788571117265.jpg")

    在注释信息下面，将新页面的跳转就可以了。  

如果有其他需求，也在这里自行处理，应该就没有问题了。

另外，运行zxing源码，可以看到它有个设置页面，也可以根据需求，集成该设置页面，或修改<span style="color:#f79646">R.xml.preferences</span>中的配置即可。