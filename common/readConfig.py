#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/3/22 14:22
#Author:Chao
import configparser
import os

path = os.path.dirname(os.path.dirname(__file__))
new_path = os.path.join(path, 'config.ini')
class readConfig(object):
    def __init__(self):
        self.config =configparser.ConfigParser()
        self.config.read(new_path,encoding='utf-8')
    # 获取某个section下面的key和value
    def getemail(self,name):
        value = self.config.get('EMAIL',name)
        return value
if __name__ == '__main__':
    readconfig = readConfig()
    print("邮箱的名字是：",readconfig.getemail('mail_user'))