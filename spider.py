# -*- coding = utf-8 -*-
# @Time: 2020/08/03 16:04
# @Author: sun_0128
# @File: spider.py
# @Software: PyCharm
from bs4 import BeautifulSoup #网页解析 获取数据
import re   #正则表达式,进行文字匹配
import urllib.request,urllib.error#指定url 获取网页数据
import xlwt #进行excel操作
import sqlite3 #进行SQLite数据库操作





def main():
    baseUrl = "https://movie.douban.com/top250?start="
    #爬取网页
    dataLsit = getData(baseUrl)
    savePath = "豆瓣电影250.xls"
    dbPath = "movie.db"
    #保存数据
    #1)excel
    saveData(dataLsit,savePath)
    #2)数据库
    saveData2DB(dataLsit,dbPath)
#爬取网页方法
findLink = re.compile(r'<a href="(.*?)">') #创建正则表达式对象
#图片链接
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S) #包含换行符
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#硬片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评论人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

def getData(baseUrl):
    dataList = []
    for i in range(0,10): #250条记录 10个分页 每页25个
        url = baseUrl+str(i*25)
        html = askURL(url)
        # 逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"): #查找符合要求的字符串 形成列表
            # print(item) #测试
            data = []#保存一部电影的所有信息
            item = str(item)
            #获取影片详情连接
            link = re.findall(findLink,item)[0] #通过正则表达式查找指定的字符串
            data.append(link)
            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle,item) #片名可能只有一个中文名
            if(len(titles) == 2):
                ctitle = titles[0]
                otitle = titles[1].replace("/","")#去掉无关符号
                data.append(ctitle)
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append("") #外文名留空
            rating = re.findall(findRating,item)[0]
            data.append(rating)
            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)
            inq = re.findall(findInq,item)
            if(len(inq) !=0):
                data.append(inq[0].replace("。","")) #可能没有
            else:
                data.append("") #留空
            bd = re.findall(findBd,item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?"," ",bd) #去掉br
            bd = re.sub('/'," ",bd) #去掉/
            data.append(bd.strip()) #去前后空格

            dataList.append(data)
    # for x in dataList:
    #     print(x,"\n")
    return dataList

#得到指定一个url的网页内容
def askURL(url):
    head = {}#伪装
    head["User-Agent"]=" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    #用户代理表示告诉服务器,我们是浏览器(本质是告诉浏览器我们可以接受什么)
    request=urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
#保存数据方法
def saveData(dataList,savePath):
    # 创建xlwt对象
    workbook = xlwt.Workbook(encoding="utf-8",style_compression=0)
    worksheet = workbook.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接","图片链接","影片中文名","影片外文名","评分","评论数","概况","相关信息")
    for i in range(0,8):
        worksheet.write(0,i,col[i]) #列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = dataList[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])
    workbook.save(savePath)  # 保存到硬盘
def saveData2DB(dataLsit, dbPath):
    init_db(dbPath) #初始化数据库
    conn = sqlite3.connect(dbPath) #打开或创建数据库
    cur = conn.cursor() #获取游标
    for data in dataLsit:
        for i in range(len(data)): #对内容进行处理
            if i ==4 or i ==5:
                continue
            data[i] = '"'+data[i]+'"'
        sql = '''
            insert into movie250(
            info_link,pic_link,cname,ename,score,rated,introduction,info)
            values (%s)
            '''%",".join(data)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()
def init_db(dbPath):
    conn = sqlite3.connect(dbPath)  # 打开或创建数据库
    # 创建数据表
    sql = """
    create table if not exists movie250(
    id INTEGER primary key autoincrement,
    info_link text,
    pic_link text,
    cname text,
    ename text,
    score numeric,
    rated numeric,
    introduction text,
    info text
    )
    """
    cur = conn.cursor() #获取游标
    cur.execute(sql) #执行sql
    cur.close() #关闭资源
    conn.close()
if  __name__ == "__main__"  :
        main()


