
# -*- coding = utf-8 -*-
# @Time: 2020/08/21 10:40
# @Author: sun_0128
# @File: testRe.py
# @Software: PyCharm

#正则表达式:字符串模式(判断字符串是否符合一定的标准)
import re
# 创建模式对象
#此处AA表示正则表达式模式
pat = re.compile("AA")
# search后面表示被校验的内容
m = pat.search("abcAA")
print(m)

# 没有模式对象
m = re.search("AA","BAAAD")
print(m)
print(re.findall("a", "Asd a sl;ka"))

# sub
print(re.sub("a","A","ABABabcd"))
# 建议加上r 不需要考虑转义内容
