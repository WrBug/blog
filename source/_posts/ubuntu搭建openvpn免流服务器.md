---
title: ubuntu搭建openVPN免流服务器
tags: 
- 免流
- openVPN
categories:
 - 杂七杂八
date: 2016-6-25 11:40:00

---
本方法集合网上的一些教程，本人亲测有效的一套教程，只支持有公网IP的ubuntu服务器
<!-- more -->
## 准备工具
1. ubuntu服务器
2. ssh终端
3. 手机一部

## openVPN服务端配置
#### 1.安装openVPN
开始前请先获取root权限
    apt-get install -y openvpn openssl
#### 2.配置VPN服务器参数
    cd /etc/openvpn/
    wget http://www.mandroid.cn/upload/2016/06/server.conf
    chmod 0755 ./*.conf
#### 3.证书制作
    #下载证书制作工具
    cd /etc/openvpn/
    wget http://www.sbwml.cn/yum/EasyRSA-2.2.2.tar.gz
    tar -zxvf EasyRSA-2.2.2.tar.gz
    #证书生成
    cd /etc/openvpn/easy-rsa/
    source vars
    ./clean-all
    ./build-ca   #一路的回车
    ./build-key-server server #一路的回车，注意最后两步需要输入y回车
    ./build-key client #一路的回车，注意最后两步需要输入y回车
    ./build-dh   #等待证书制作
#### 4.证书下载
Windows上可以使用WinSCP进入/etc/openvpn/easy-rsa/keys目录，下载ca.crt、client.crt、client.key三个文件到自己的电脑上
#### 5. 配置/启用端口转发
    apt-get install squid3 -y #没有squid3的可以安装squid
    cd /etc/squid3/
    rm -f ./squid.conf
    wget http://www.mandroid.cn/upload/2016/06/squid.conf
    chmod 0755 squid.conf
    squid3 -z
    squid3 -s
#### 6. 开启路由转发
    vi /etc/sysctl.conf
修改参数

    net.ipv4.ip_forward = 1
保存

    sysctl -p
#### 7. 配置防火墙规则
    iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE
    iptables -A INPUT -p TCP --dport 5200 -j ACCEPT  #OpenVPN服务端口
    iptables -A INPUT -p TCP --dport 80 -j ACCEPT  #squid转发端口
    iptables -A INPUT -p TCP --dport 22 -j ACCEPT
    iptables -t nat -A POSTROUTING -j MASQUERADE
    iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
    modprobe ip_tables
#### 8. 启动/重启openVPN
    service openvpn start  #启动OpenVPN
    service openvpn restart  #重启OpenVPN
## 9.openVPN客户端配置
 下载配置文件模板[client.ovpn](http://www.mandroid.cn/upload/2016/06/client.ovpn)，编辑文件，填写免流代码，服务器ip，CA证书（ca.crt文件里面的内容）,客户证书(client.crt文件里面-----BEGIN CERTIFICATE----- 开始，-----END CERTIFICATE-----结束的内容，包括这两行)，客户密钥（client.key的内容）。完成后发送到手机上，打开openVPN客户端载入文件连接即可
 