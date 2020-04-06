# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:55:25 2017

@author: xiabing
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")
# images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
# for image in images:
#     print(image["src"])

"""
获取属性
对于一个标签对象 可用这个方法获取它的全部属性  myTag.attrs    返回的是一个字典对象
	例如:   要获取图片的资源位置src
					myImgTag.attrs["src"]
"""


"""
		Lambda表达式
	Lambda表达式 本质上就是一个函数，可以作为其他函数的变量使用
"""
print(bsObj.findAll(lambda tag:len(tag.attrs) == 2))

