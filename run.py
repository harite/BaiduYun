'''
Created on DEC 5,2014

@author: Cake
'''

import httplib
import urllib2

BaiduYunServer = "pcs.baidu.com"
#ProxyServer = "cnnjproxy02-gfw.tw.trendnet.org"
ProxyServer = "cnnjproxy-ha.tw.trendnet.org"

ProxyPort = "8080"
Proxy = ProxyServer + ":" + ProxyPort

ClientId = ""
ResponseType = "code"


connect = httplib.HTTPConnection(Proxy)
URL = "http://" + BaiduYunServer
connect.request("GET", "https://pcs.baidu.com/oauth/2.0/authorize?client_id=vosP7yEMzEkrlpi57lSV7QjX&response_type=code&redirect_uri=http%3A%2F%2Fwww.baidu.com")
result = connect.getresponse()
print result.status, result.reason
print result.read()