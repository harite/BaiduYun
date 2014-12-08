#! /usr/bin/env python
'''
Created on DEC 5,2014

@author: Cake
'''

import httplib
import urllib2

BaiduYunServer = "pcs.baidu.com"
ProxyServer1 = "cnnjproxy02-gfw.tw.trendnet.org"
ProxyServer2 = "cnnjproxy-ha.tw.trendnet.org"
ProxyServer3 = "10.64.8.8"

Proxy = (
    "cnnjproxy02-gfw.tw.trendnet.org:8080",
    "cnnjproxy-ha.tw.trendnet.org:8080",
    "10.64.8.8"
)

print "Using Proxy: " + Proxy[1]



ProxyPort = "8080"
#Proxy = ProxyServer + ":" + ProxyPort

Prefix = "/oauth/2.0/authorie?" #prefix of authorize


ClientId = "vosP7yEMzEkrlpi57lSV7QjX" #API key 
ResponseType = "code"
RedirectUri = "http%3A%2F%2Fwww.baidu.com" #the page that after authorization succeed

connect = httplib.HTTPConnection(Proxy[1])
URL = "https://" + BaiduYunServer + Prefix + "client_id=" + ClientId + "&response_type=" + ResponseType + "&redirect_uri=" + RedirectUri
#connect.request("GET", "https://pcs.baidu.com/oauth/2.0/authorize?client_id=vosP7yEMzEkrlpi57lSV7QjX&response_type=code&redirect_uri=http%3A%2F%2Fwww.baidu.com")
connect.request("GET", URL)
result = connect.getresponse()
print result.status, result.reason
print result.read()
