# -*- coding = utf-8 -*-
# @Time: 2020/08/22 20:18
# @Author: sun_0128
# @File: testXwlt.py
# @Software: PyCharm
import xlwt
#创建xlwt对象
workbook = xlwt.Workbook(encoding="utf-8")

worksheet = workbook.add_sheet('sheet1')#创建工作表
# worksheet.write(0,0,"hello") #行 列 内容
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d x %d = %d"%(i+1,j+1,(i+1)*(j+1)))
workbook.save("99.xls") #保存到硬盘