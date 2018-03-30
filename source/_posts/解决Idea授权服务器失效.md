---
title: 解决Idea授权服务器失效
date: 2018-03-08 12:20:08
categories:
- 杂七杂八
tags: 
- IntelliJ Idea
- 激活
- 注册码
---

> 最近有很多朋友反映授权服务器无法授权了，经过研究，发现是域名被屏蔽了。所以解决方案是通过自己域名来授权

<!-- more -->

如果文章对你有用请在下方打赏，打赏费将用于服务器维护


**最近阿里云搞活动。服务器99一年，通过降配最高可以达到8年（需要选择成功节点），平均35一年，有兴趣的可以去撸一撸，自己做做网站的都不错**
[点击这里购买云服务器](https://promotion.aliyun.com/ntms/act/group/team.html?group=46gd3KjcLz)
### ip列表

```
45.77.198.219
45.63.16.42
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




