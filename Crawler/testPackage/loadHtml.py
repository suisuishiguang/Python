# -*- coding: UTF-8 -*-
# urllib2下载网页的三种方法
import cookielib, urllib2

url = "http://baidu.com"
print "第一种方法"
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print "第二种方法"
request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print "第三种方法"
cj = cookielib.CookieJar()  # 创建cookiejar实例对象
print cj
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
#print response1.getCode()

print response3.read()