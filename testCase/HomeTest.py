#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/3/15 11:53
#Author:Chao

from common.Driver import startUp
import unittest
import time
from common.MyTest import MyTest
from common.Driver import startUp
from common.readData import readExcel
class HomTest(MyTest):
    def test_weiToutiao(self):
        self.driver.find_element_by_id('com.ss.android.article.news:id/bth').click()
        time.sleep(3)
        self.driver.find_elements_by_class_name('android.widget.TextView')[1].click()
        time.sleep(3)
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys("最近的疫情怎么样呀")
        time.sleep(3)
        self.driver.find_element_by_id('com.ss.android.article.news:id/a_y').click()
        time.sleep(3)
    def test_search(self):
        re = readExcel()
        # 获取当前的类名和方法名
        Classname = self.__class__.__name__
        Methodname = self._testMethodName
        data = re.read(Classname,Methodname)
        for i in data:
            self.driver.find_element_by_id('com.ss.android.article.news:id/bt5').click()
            time.sleep(3)
            self.driver.find_element_by_id('com.ss.android.article.news:id/y6').send_keys(i)
            time.sleep(3)
            self.driver.find_element_by_id('com.ss.android.article.news:id/y3').click()
            time.sleep(5)
if __name__ == '__main__':
    unittest.main()
