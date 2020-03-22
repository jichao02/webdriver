#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/3/22 15:42
#Author:Chao
'''
1-导入xlrd
2-打开excsl
3-定位sheet页
4-找到对应的行，列：读取全部行数据，根据类名和方法名读取需要的数据
5-返回
'''
import xlrd,os
class readExcel(object):
    def __init__(self):
        readbook =xlrd.open_workbook("D:\\vip\webdriver\\testData\data.xlsx")
        self.sheet = readbook.sheet_by_index(0)
    def read(self,classname,methodname):
        for i in range(1,self.sheet.nrows):
            row_value = self.sheet.row_values(i)
            if row_value[1] == classname and row_value[2] == methodname:
                self.data_list.append(self.sheet.row_values(i))
        return self.data_list
if __name__ == '__main__':
    re = readExcel()







