# -*- coding = utf-8 -*-
# @Time: 2020/08/03 18:45
# @Author: sun_0128
# @File: testBs4.py
# @Software: PyCharm
from bs4 import BeautifulSoup

file = open("baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")
#拿第一个标签
# print(bs.title)
# print(bs.a)
# print(bs.head)
#1.Tag 标签和内容 只能拿到找到的第一个
print(bs.title)
#2.标签里的内容
print(bs.title.string)
#3.标签里的属性
print(bs.a.attrs)
#4.整个文本
print(bs)

#注释 Comment 输出的内容不包含注释符号
print(bs.a.string)

print("*"*30)

#文档的遍历
print(bs.head.contents)#列表
#文档的搜索

#1)find_all 查找所有
#字符串过滤 会查找与字符串完全匹配的内容
print("*"*30)
t_list = bs.find_all("a")
print(t_list)
print("*"*30)
#2)正则表达式搜索 使用search()方法匹配内容
import re
t_list2 = bs.find_all(re.compile("a"))
print(t_list2)
print("*"*30)

# 传入一个函数,根据一个函数的要求来搜索
def name_is_exists(tag):
    return tag.has_attr("name")
t_list3 = bs.find_all(name_is_exists)
print(t_list3)
print("*"*30)

#2 keywords args 参数
t_list4 = bs.find_all(id="head")
print(t_list4)
print("*"*30)

#3. text参数
t_list5 = bs.find_all(text=["hao123","地图","贴吧"])
print(t_list5)
print("*"*30)

#4. limit参数 取几条数据
t_list = bs.find_all("a",limit=3)
# css 选择器
# 指定标签
t_list = bs.select("title")
# 指定类名
t_list = bs.select(".mnav")
#指定id
t_list = bs.select("#u1")
#属性 a标签的属性
t_list = bs.select("a[class='bri']")
#子标签
t_list = bs.select("head > title")
#兄弟节点
t_list = bs.select(".mnav ~ .bri")
print(t_list[0].get_text())
