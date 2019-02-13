# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 23:59:28 2019

@author: Administrator
"""

# 这个程序是用来下载网站上的视频（只需要网址就可以了）
#目前只测试过在bilibili网站下载视频，据说you-get可以爬取很多网站的高清视频

import you_get
import os
import time

#设置文件存放的目录
os.chdir("F:\\零基础入门学习Web开发")

#设置一个函数来下载网站上的视频。
def getMp4(urlList):
    #设置一个cmd命令行列表
    cmd_list = [] 
    for url in urlList: 
        cmds = 'you-get' + " " + url
        cmd_list.append(cmds) #写入cmd命令行列表中
    #在系统中运行每一个cmd命令行，然后暂停一秒    
    for each in cmd_list:
        time.sleep(1)
        os.system(each)

#获取视频网站列表
urlList = []
#如果是下载一系列教程，可以通过网站之间的不同之处，利用for循环来快速编写网站列表。
for i in range(1,25):
    url='https://www.bilibili.com/video/av21786264/?p='+str(i)
    urlList.append(url)
    
#运行函数获取视频。
getMp4(urlList)

os.system("shutdown -s -t 1")



