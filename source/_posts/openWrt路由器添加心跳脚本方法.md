---
title: OpenWrt路由器添加心跳脚本方法
tags: 闪讯
categories:
 - 闪讯相关
date: 2016-4-12 21:57:00

---

<font color='red'>**另一篇文章：**</font>[*OpenWrt路由器添加心跳脚本方法(python)*](/2016/04/01/openWrt%E8%B7%AF%E7%94%B1%E5%99%A8%E6%B7%BB%E5%8A%A0%E5%BF%83%E8%B7%B3%E8%84%9A%E6%9C%AC%E6%96%B9%E6%B3%95%28python%29/index.html)
该方法目前只针对部分openwrt路由器，后面会持续更新，请关注我的博客，目前支持ramips和mips架构的路由器
<!-- more -->
### 准备工具
- openwrt路由器
- winscp
- putty

### 步骤
#### 检查CPU型号
打开putty，命令：`cat /proc/cpuinfo` 
如cpu型号为ramips和mip可使用该方法，如果不是可以看博文*OpenWrt路由器添加心跳脚本方法(python)*
#### 配置心跳脚本
[http://pan.baidu.com/s/1pKLUx1x](http://pan.baidu.com/s/1pKLUx1x)，下载路由器对应的**文件夹**，每个文件夹里面有三个文件，使用winscp将文件夹上传到`/var`根目录，**将文件夹名改为`heart`**，修改文件夹以及每个文件的权限为777
#### 校验
putty输入 `sh /var/heart/heart.sh` ,
正常情况会出现以下内容，最后一行为**success**表示发送成功：
![](/upload/2016/04/20160412215212.png)
### 配置定时任务
方法一：
编辑/etc/crontabs/root 文件，添加行
`*/3 * * * * /var/heart/heart.sh`
方法二：
前往路由器后台界面定时任务处添加行
`*/3 * * * * /var/heart/heart.sh`

最后重启即可