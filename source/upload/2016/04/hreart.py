#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    在线获取心跳数据并发送
'''
__author__='sxm'
import urllib2,time,json,re,hashlib,socket,commands
#获得外网IP
def get_ip():
    try:
        res=urllib2.urlopen(URL+'/index.php/heart/GetIp',timeout=2000)
    except:
        return None
    if res.getcode()!=200:
        return None
    re=res.read().decode('gbk').encode('utf8')
    res.close()
    #re=re[re.rfind('{'):re.find('}')+1]
    return json.loads(re)
#发送心跳
def send_pack(data,ip,port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        print str(len(data))+'(86+your ShanXun Acount)'
        sock.sendto(data,(ip,port))
    except Exception, e:
        log('ERROR: '+time.asctime( time.localtime(time.time()) )+' 发送数据失败\r\n')
        exit()
    finally:
        sock.close()
    return

#获取服务器数据
def get_data(strdata):
    try:
        respone=urllib2.urlopen(URL+'/index.php/heart/getByRouter/?'+strdata)
    except:
        return None
    if respone.getcode()!=200:
        return None
    data=respone.read()
    respone.close()
    return data
def log(logStr):
    with open('/tmp/sxlog.txt', 'a') as f:
        f.write(logStr+'\r\n')
if __name__=='__main__':
    global URL
    URL='http://sx.mandroid.cn'
    user=commands.getoutput('uci get network.wan.username')
    #user='15355498807@DZKD.XY'
    if user==None:
        log('ERROR: '+time.asctime( time.localtime(time.time()) )+' GET USER ERROR\r\n')
        exit()
    print user
    ip=get_ip()
    if ip==None:
        log('ERROR: '+time.asctime( time.localtime(time.time()) )+' GET IP ERROR\r\n')
        exit()
    ip_info=ip["ip"]
    print ip_info
    sendstr='user='+user+'&ip='+ip_info
    data=get_data(sendstr)
    #data=data[data.rfind('{'):data.find('}')+1]
    #print data
    data=json.loads(data)
    status=data["status"]
    if status==200:
        data=data["data"]
        #data=json.loads(data)
        pack_data=data["packData"]
        send_ip=data["sendIp"]
        send_port=data["sendPort"]
        import base64
        data=base64.b64decode(pack_data)
    else:
        log('ERROR: '+time.asctime( time.localtime(time.time()) )+'GET DATA ERROR  code='+data['message']+'\r\n')
        exit()
    send_pack(data.strip(),send_ip,send_port)
    #log('LOG: '+time.asctime(time.localtime() )+'success ')
