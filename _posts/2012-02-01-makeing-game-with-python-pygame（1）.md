---
layout: default
title: Makeing Game with Python & Pygame（1）
---
# 一个简单的Pygame程序 #
	__author__ = 'Yiner'
	# -*- coding: utf-8 -*-
	import pygame, sys
	from pygame.locals import *
	#以上为载入需要的模块
	
	pygame.init()#初始化模块
	
	DISPLAYSURF = pygame.display.set_mode((100, 100))#创建一个100*100像素的窗口 返回一个pygame.Surface的对象
	pygame.display.set_caption('Hello Pygame World!')#设置窗口的标题
	
	while True: #游戏主循环
	    for event in pygame.event.get():#pygame.event.get():接收鼠标键盘等的动作 返回一个事件列表
	
	        if event.type == QUIT:#type表示事件的类型 QUIT是pygame.locals下的一个常变量 pygame.locals.QUIT
	
	            pygame.quit()#与pygame.init()相对应 基本上可以不写的 但是在IDLE下不写会报错
	
	            sys.exit()#退出Pygame程序
	            pygame.display.update()#通过绘制Surface对象来更新画面 

![一个简单的Pygame程序](http://bcs.duapp.com/blog-pyiner/28_XK42CUHGF1KZ2-300x243.jpg?sign=MBO:528b10b38a1b368b5a572d8d459f541b:68MV4JTsg0sFgIfLyTheyz14cD8%3D)