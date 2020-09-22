# -*- coding = utf-8 -*-
# @Time: 2020/08/03 16:36
# @Author: sun_0128
# @File: testurllib.py
# @Software: PyCharm
import urllib.request
#获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))#utf-8解码

#获取一个post请求 hhtpbin.org 测试
import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))


#超时
# try:
#     response = urllib.request.urlopen("http://www.baidu.com/get",timeout=1)
#     # print(response.read().decode("utf-8"))
#     # print(response.getheaders())
#     print(response.getheader("Server"))
#     # print(response.status)
# except urllib.error.URLError as e:
#     print("time out")

url = "https://movie.douban.com/top250?start=/post"
headers = {
    "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
data = bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))