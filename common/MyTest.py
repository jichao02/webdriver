#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/3/22 12:09
#Author:Chao
'''
1-继承 unittest父类，方便 testcase调用
2-初始化和清理方法
'''
import unittest
from common.Driver import startUp
import time
class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = startUp()
    def setUp(self) -> None:
        self.driver.launch_app()
        time.sleep(5)
    def tearDown(self) -> None:
        self.driver.close_app()
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()
if __name__ == '__main__':
    unittest.main()