#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/3/15 11:53
#Author:Chao

from common.Driver import startUp
import unittest
import time
class Case(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = startUp()
    def test_sendToutiao(self):
        self.driver.find_element_by_id('com.ss.android.article.news:id/bth').click()
        time.sleep(3)
        self.driver.find_elements_by_class_name('android.widget.TextView')[1].click()
        time.sleep(3)
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys("最近的疫情怎么样呀")
        time.sleep(3)
        self.driver.find_element_by_id('com.ss.android.article.news:id/a_y').click()
        time.sleep(3)
    def tearDown(self) -> None:
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
