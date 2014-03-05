---
layout: default
title: Makeing Game with Python & Pygame（2）
---
# Surface对象和程序的窗口 #
Surface对象代表了一个2D的矩阵图像

Surface对象的像素能背Pygame绘图函数所调用 然后显示在屏幕上

窗口的边框 标题和按钮不属于Surface对象

Surface对象中有一种特别的对象 是由pygame.display.set_mode()返回的对象 称为display Surface

display Surface对象会在调用pygame.display.updata()函数的时候被画在屏幕上 绘制display Surface对象到屏幕上是非常快的（因为它存在于内存中）

当你在游戏的主函数中Surface对象中加入什么（完成了一个新的画面） 那么这个画面就会被绘制到屏幕上 电脑绘制画面的速度是非常快的 大约每秒30次——30FPS 每一个画面叫做一帧

# 色彩 #
电脑上所有的颜色都由红绿蓝三种颜色组成 与绘画的三原色红蓝黄不同是因为电脑上的色彩是以光的形式表现的

在Pygame中 我们用一个包含三个整型数的元组表示一个颜色 元组中元素的值在0到255之间（如果大于255或者为负数 会引发 “ValueError: invalid color argument”异常） 这样的元组被称为RGB值
一些常用的颜色

	Color	RGB Values
	Aqua	(  0, 255, 255)
	Black	(  0,   0,   0)
	Blue	(  0,   0, 255)
	Fuchsia	(255,   0, 255)
	Gray	(128, 128, 128)
	Green	(  0, 128,   0)
	Lime	(  0, 255,   0)
	Maroon	(128,   0,   0)
	Navy Blue	(  0,   0, 128)
	Olive	(128, 128,   0)
	Purple	(128,   0, 128)
	Red	(255,   0,   0)
	Silver	(192, 192, 192)
	Teal	(  0, 128, 128)
	White	(255, 255, 255)
	Yellow	(255, 255,   0)
# 透明色 #
扩展原来的三元组为四元组 最后一个元素的值（alpha value） 在0~255之间 0表示全透明 255表示不透明
如果要使用透明色 那么必须通过convert_alpha()方法创建一个Surface对象
例如：anotherSurface = DISPLAYSURF.convert_alpha()
颜色类

	>>> import pygame
	>>> pygame.Color(255, 0, 0)
	(255, 0, 0, 255)
	>>> myColor = pygame.Color(255, 0, 0, 128)
	>>> myColor == (255, 0, 0, 128)
	True
	>>>
# 矩形 #
由一个四元组表示 （左上角的横坐标，左上角的纵坐标，宽，高）
矩形对象
	
	>>> import pygame
	>>> spamRect = pygame.Rect(10, 20, 200, 300)
	>>> spamRect == (10, 20, 200, 300)
	True
矩形对象有很多属性 矩形对象可以根据用户修改的属性值 去自动计算相关联的其他属性值
	
	>>> spamRect.right
	210
	>>> spam.right = 350
	>>> spam.left
	150
## 矩形对象的一些属性 ##

	Attribute Name	Description
	myRect.left	The int value of the X-coordinate of the left side of the rectangle.
	myRect.right	The int value of the X-coordinate of the right side of the rectangle.
	myRect.top	The int value of the Y-coordinate of the top side of the rectangle.
	myRect.bottom	The int value of the Y-coordinate of the bottom side.
	myRect.centerx	The int value of the X-coordinate of the center of the rectangle.
	myRect.centery	The int value of the Y-coordinate of the center of the rectangle.
	myRect.width	The int value of the width of the rectangle.
	myRect.height	The int value of the height of the rectangle.
	myRect.size	A tuple of two ints: (width, height)
	myRect.topleft	A tuple of two ints: (left, top)
	myRect.topright	A tuple of two ints: (right, top)
	myRect.bottomleft	A tuple of two ints: (left, bottom)
	myRect.bottomright	A tuple of two ints: (right, bottom)
	myRect.midleft	A tuple of two ints: (left, centery)
	myRect.midright	A tuple of two ints: (right, centery)
	myRect.midtop	A tuple of two ints: (centerx, top)
	myRect.midbottom	A tuple of two ints: (centerx, bottom)