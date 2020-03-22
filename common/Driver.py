#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/3/15 17:52
#Author:Chao

from appium import webdriver
import time
def startUp():
    print("----启动中，，，----")
    desire_caps = {
        "deviceName": "127.0.0.1:21503",
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "appPackage": "com.ss.android.article.news",
        "appActivity": "com.ss.android.article.news.activity.MainActivity",
        "noReset": True,
        "unicodeKeyboard": True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
    print("----启动成功----")
    time.sleep(10)
    return driver
if __name__ == '__main__':
    driver = startUp()
    time.sleep(3)
    driver.quit()






