# -*- coding = utf-8 -*-
# @Time: 2020/08/22 20:42
# @Author: sun_0128
# @File: testSQLite.py
# @Software: PyCharm
import sqlite3

conn = sqlite3.connect("movie.db") #打开或创建数据库文件

print("成功打开数据库")
c = conn.cursor()#获取游标
sql = """
    create table if not exists company
        (id int primary key not null ,
        name text not null,
        age int not null,
        address char(50),
        salary real);
"""
sql1 = """
 insert into company(id,name,age,address ,salary) values
 (1,'张三',32,'成都',8000);
"""
sql2 = "select * from movie250"

a= c.execute(sql2)#执行sql语句
for row in a:
    print(row)
conn.commit()#提交
conn.close()#关闭数据库连接

