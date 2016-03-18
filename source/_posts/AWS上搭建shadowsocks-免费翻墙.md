---
title: AWS上搭建shadowsocks 免费翻墙
tags: []
date: 2016-02-29 14:47:07
---

hadowsocks类似goagent，是一种快速隧道代理，帮助你绕过防火墙。shadowsocks需要使用自己的服务器，当然选择不同价格的服务器决定了服务的质量:-)
<!-- more -->
优点：

1.  可以免费：shadowsocks可以利用免费的Aws EC2，公有服务器还是不考虑吧，毕竟时间更宝贵。

2.  表现稳定：有过使用goagent的经验，经常会丢包

3.  速度较快：还是那句话，一分钱一分货

4.  多平台支持：感谢开源，无论Linux，win*，MacOS，iOS，Android平台均可以安装shadowsocks客户端

<span style="font-size: 20px;">1.注册</span>

1.  注册AWS账号，需要信用卡（淘宝上有1美元账户，或者申请[全球付虚拟信用卡](https://www.globalcash.hk/))

2.  进入[aws主页](http://aws.amazon.com/cn/)，按照提示完成注册，然后需要进一步通过手机验证_“Identity Verification by Telephone”_，输入电话号码后点击_“call me now”_，稍后Amazon便会有电话拨来，按照提示在电话上输入屏幕上的_“Your PIN：”_给出的四个数字即可。

3.  之后选择_Amazon Support Plan_，这里选择_Basic（Free）_，注册成功后会进入欢迎界面，选择_“启动Aws管理控制台”_。

<span style="font-size: 20px;"></span><span style="font-size: 20px;">2.创建实例（推荐东京节点）</span>

![awsec201.png](/upload/2016/02/201602291456728783308021.png "201602291456728783308021.png")

<span style="color: rgb(85, 85, 85); font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; background-color: rgb(255, 255, 255);">选择</span>_Amazon系统映像_<span style="color: rgb(85, 85, 85); font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; background-color: rgb(255, 255, 255);">(AMI)，这里选择</span>_“Ubuntu Server 14.04 LTS”_<span style="color: rgb(85, 85, 85); font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; background-color: rgb(255, 255, 255);">，如下图：</span>

<span style="color: rgb(85, 85, 85); font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; background-color: rgb(255, 255, 255);">![QQ截图20160229145350.png](/upload/2016/02/201602291456728851354710.png "201602291456728851354710.png")</span>

<span style="color: rgb(85, 85, 85); font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; background-color: rgb(255, 255, 255);">
</span>

_<span style="color: rgb(85, 85, 85); font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; background-color: rgb(255, 255, 255);">一路下一步到配置安全组（添加一个规则，端口<span style="font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; color: rgb(255, 0, 0); background-color: rgb(255, 255, 255);">443</span>，也可以自定义，来源<span style="font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; color: rgb(255, 0, 0); background-color: rgb(255, 255, 255);">任何位置</span>）</span>_

<span style="color: rgb(85, 85, 85); font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; background-color: rgb(255, 255, 255);">
</span>

<span style="color: rgb(85, 85, 85); font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; background-color: rgb(255, 255, 255);">![blob.png](/upload/2016/02/201602291456728901300663.png "正在上传...")</span>

<span style="font-family: &#39;Open Sans&#39;; line-height: 26px; color: rgb(255, 0, 0); font-size: 20px; background-color: rgb(255, 255, 255);">继续步骤创建完成，进入控制面板的弹性ip分配公网地址，绑定刚申请的实例（这步很重要）</span>

<span style="font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; color: rgb(255, 0, 0); background-color: rgb(255, 255, 255);">
</span>

<span style="color: rgb(85, 85, 85); font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; background-color: rgb(255, 255, 255);">![blob.png](/upload/2016/02/201602291456729113103878.png "正在上传...")</span>

<span style="color: rgb(85, 85, 85); font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; background-color: rgb(255, 255, 255);">
</span>

<span style="color: rgb(85, 85, 85); line-height: 26px; font-size: 20px; font-family: &#39;Microsoft YaHei&#39;; background-color: rgb(255, 255, 255);">3.配置shadowsocks</span>

<span style="color: rgb(85, 85, 85); line-height: 26px; font-size: 20px; font-family: &#39;Microsoft YaHei&#39;; background-color: rgb(255, 255, 255);">
</span>

_<span style="color: rgb(85, 85, 85); font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; background-color: rgb(255, 255, 255);">登录ssh（</span><span style="color: rgb(85, 85, 85); font-family: &#39;Open Sans&#39;; font-size: 16px; line-height: 26px; background-color: rgb(255, 255, 255);">[ssh使用教程](https://docs.aws.amazon.com/zh_cn/console/ec2/instances/connect/docs)），执行以下命令：</span>_
<pre class="brush:cf;toolbar:false">1. sudo -s //获取超级管理员权限
2. apt-get update //更新apt-get
3. apt-get install python-pip //安装python包管理工具pip
4. pip install shadowsocks // 安装shadowsocks</pre><pre class="brush:cf;toolbar:false">nano /etc/shadowsocks.json  //配置文件</pre>

_
_

_添加以下代码：_

_
_
<pre class="brush:cf;toolbar:false">{
    &quot;server&quot;:&quot;0.0.0.0&quot;,
    &quot;server_port&quot;:在创建实例安全组时添加的端口号（比如443）,
    &quot;local_address&quot;:&quot;127.0.0.1&quot;,
    &quot;local_port&quot;:1080,
    &quot;password&quot;:&quot;连接密码&quot;,
    &quot;timeout&quot;:300,
    &quot;method&quot;:&quot;aes-256-cfb&quot;,
    &quot;fast_open&quot;:false
}</pre><pre class="brush:cf;toolbar:false">ssserver -c /etc/shadowsocks.json -d start //启动shadowsocks</pre>

<span style="font-size: 20px;">4.shadowsocks客户端下载：</span>

[https://shadowsocks.org/en/index.html](https://shadowsocks.org/en/index.html)

配置截图：

![blob.png](/upload/2016/02/201602291456738265125261.png "正在上传...")