---
title: 闪讯WiFi助手2.3开源版，带心跳，提供心跳接口
tags: 闪讯
categories:
- 闪讯
toc: true
date: 2016-3-19 15:40:00
---

## 版本说明

1. 修复对话框权限
2. 移除VIP权限
3. 移除金币功能
4. 完全免费
<!-- more -->
## 心跳接口

URL：   [
][1]


METHOD：    GET/POST

QUERY： 
  user=[闪讯账号]
    ip=[IP地址]
    
示例：[http://sx.mandroid.cn/index.php/heart/getByRouter?user=123456@ABC.XY&ip=192.168.1.1][2]

RESPONSE：

    {
    "status": 200,
    "data": {
        "packData": "U04AYwOCQpY85mPaVnecguWKlDde4wIAB8CoAQEDAAwxLjIuMTguMjgUACNiNTcyYjI1NjEwODA4ZGE1N2QyY2Y0YWEyMGViZmE2ORIAB1br6zcBABAxMjM0NTZAQUJDLlhZ",  //base64encode
        "sendIp": "115.239.134.167",
        "sendPort": 8080
        }
    }
    
## 项目地址
github:[https://github.com/wangtao2132/wtshanxun][3]
豌豆荚：[http://www.wandoujia.com/apps/cn.mandroid.wtshanxun][4]


  [1]: http://sx.mandroid.cn/index.php/heart/getByRouter
  [2]: http://sx.mandroid.cn/index.php/heart/getByRouter?user=123456@ABC.XY&ip=192.168.1.1
  [3]: https://github.com/wangtao2132/wtshanxun
  [4]: http://www.wandoujia.com/apps/cn.mandroid.wtshanxun