---
title: 解决Idea授权服务器失效
date: 2018-06-04 16:20:08
categories:
- 杂七杂八
tags: 
- IntelliJ Idea
- 激活
- 注册码
---

> 最近有很多朋友反映授权服务器无法授权了，经过研究，发现是域名被屏蔽了。本文提供两种解决方案
<font color='red'>7月30日新增两个地址，方案二教程修改</font>

<!-- more -->


如果文章对你有用请在下方打赏，打赏费将用于服务器维护，推荐使用方案一，可以直接使用

## 方案一

使用如下地址：

```
http://*.idea.wrbug.com
http://*.idea1.wrbug.com
http://*.jetbrains.xyz
http://*.jetbrains.fun
```


其中*代表任意数字或字母组合,如 `123.idea.wrbug.com` ,`abc.idea.wrbug.com` ,`abc123.idea.wrbug.com`


## 方案二

### ip列表

```
//使用ping获取
ping www.jetbrains.fun -t 4

ping www.jetbrains.xyz -t 4

```

### 设置dns解析
将自己的域名<font color='red'>[没有域名看文章下面的神器免费域名]</font>添加一个A记录到ip列表中任一ip即可，如添加域名：xx.xx.com，成功后访问xx.xx.com，如果跳转到https://www.wrbug.com 说明已经解析成功，然后到idea里的manager license里,填入域名即可

![](/upload/2018/03/WX20180308-122718@2x.png)

### 申请免费域名
申请网址：[http://www.dot.tk/zh/index.html](http://www.dot.tk/zh/index.html)

这里使用tk免费域名，土豪也可以使用收费域名。进入到申请页。输入一个域名，点击旁边的检查可用性检查是否被注册,这里使用wrbugtest.tk为例

![](/upload/2018/03/WX20180308-120955.png)

下个页面会出现一些后缀的域名，点击**现在获取**将域名加入购物车，然后点击完成。

![](/upload/2018/03/WX20180308-121025.png)

点击完成后会跳转到freenom的页面，然后按照下图进行配置，hostname 自己定义，ip address 使用 上面的ip列表

![](/upload/2018/03/WX20180308-121152.png)

点击**Continue**后，有账号的可以直接登录。没账号的使用邮箱验证，然后会发送一个邮件到邮箱里，点开后开始配置个人信息，设置好个人信息后。点击**Complete Order**即可完成注册。稍后可以通过访问上面设置的hostname，如果跳转到https://www.wrbug.com 说明已经解析成功，然后到idea里的manager license里,填入域名即可




