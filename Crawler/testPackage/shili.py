# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import re
html_doc  =  """
<html> <head> <title>睡鼠的故事</ title> </ head>
<body>
<p class ="title"> <b>睡鼠的故事</ b> </ p>

<p class =“story”>从前有三个小姐妹; 他们的名字是
<a href="http://example.com/elsie" class="sister" id="link1"> Elsie </a>，
<a href ="http://example.com/lacie" class="sister" id ="link2"> Lacie </a>和
<a href="http://example.com/tillie" class="sister" id="link3"> Tillie </a>;
他们住在井底。</ p>

<p class ="story"> ... </p>
"""

# 网页解析器—— BeautifulSoup语法
# 一、创建BeautifulSoup对象
# 根据HTML网页字符串创建BeautifulSoup对象
# soup=BeautifulSoup(
#     html_doc,                HTML文档字符串
#     'html.parser'            HTML解析器
#     from_encoding='utf-8'    HTML文档的编码
# )
# 二、搜索节点（find_all;find）
# 方法：find_all(name,attr,string)节点的名字，属性，节点的文字
# 三、访问节点信息
# 得到节点<a href='1.html'>Python</a>
# 获取查找到的节点的标签名称  node.name
# 获取查到的节点a的href属性   node['href']
# 获取查找到的a节点的链接文字   node.get_text()
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
print '获取所有的链接'
links = soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()

#获取locie的链接
print '获取href=lacie的链接'
link_node = soup.find('a',href = 'http://example.com/lacie')
print link_node.name, link_node['href'], link_node.get_text()

#正则表达式
print '正则表达式匹配'
link_node = soup.find('a', href=re.compile(r"ill"))
print link_node.name, link_node['href'], link_node.get_text()

print 'p段落文本内容' #class是python的关键字，所以需要加_线
p_node = soup.find('p',class_ = "story" )
print p_node.name, p_node.get_text()
