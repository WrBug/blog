---
title: OpenWrt路由器添加心跳脚本方法
tags: 闪讯
categories:
 - 闪讯相关
date: 2016-4-1 10:57:00
---

该方法适用于python环境下的openwrt路由器，其他方法请自行测试。
<!-- more -->

### 准备工具
- openwrt路由器（最少需要16Mflash）
- winscp
- putty

### 步骤
#### 安装python环境（有的可以忽略）
打开putty，连上路由器终端，输入以下命令

    wget -c http://downloads.openwrt.org.cn/backfire/10.03.1/brcm63xx/packages/libffi_3.0.9-1_brcm63xx.ipk
    wget -c http://downloads.openwrt.org.cn/backfire/10.03.1/brcm63xx/packages/python-mini_2.6.4-3_brcm63xx.ipk
    wget -c http://downloads.openwrt.org.cn/backfire/10.03.1/brcm63xx/packages/python_2.6.4-3_brcm63xx.ipk
安装这几个包
    opkg install libffi_3.0.9-1_brcm63xx.ipk
    opkg install python-mini_2.6.4-3_brcm63xx.ipk
    opkg install python_2.6.4-3_brcm63xx.ipk
检验是否配置成功
    输入命令 `python -V` ,如出现版本号即安装成功
#### 下载心跳脚本
[下载地址](/upload/2016/04/heart),使用winscp放到路由器/usr/bin文件夹,也可以存放点任意位置，本文以/usr/bin为例
或者使用putty切换到/usr/bin(命令：`cd /usr/bin`)。输入命令`wget -c http://www.mandroid.cn/upload/2016/04/heart`
##### 检验
putty输入 `python /usr/bin/heart`
正常情况会出现以下内容，最后一行的值为检验心跳是否正确的判断，等于86+闪讯账号长度：
![](/upload/2016/04/20160401115146.png)
### 配置定时任务
在/usr/bin新建文本 `heart.sh` , 文本内容 `python /usr/bin/heart`，保存 。
编辑/etc/crontabs/root 文件，添加行
`*/3 * * * * /usr/bin/heart.sh`

重启即可
