---
layout: default
title: Making Games with Python & Pygame （5）
---
# 字体 #
	import pygame, sys
	from pygame.locals import *
	
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((400, 300))
	pygame.display.set_caption('Hello World!')
	
	WHITE = (255, 255, 255)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 128)
	
	fontObj = pygame.font.Font('freesansbold.ttf', 32)
	textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (200, 150)
	
	while True: # main game loop
	    DISPLAYSURF.fill(WHITE)
	    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	    for event in pygame.event.get():
	        if event.type == QUIT:
	            pygame.quit()
	            sys.exit()
	    pygame.display.update()

![](http://bcs.duapp.com/blog-pyiner/J3SXIX_BOLM28FFG9E.jpg?sign=MBO:528b10b38a1b368b5a572d8d459f541b:q8xrCvHkYlNA%2BzGnCyqBOpKpAIw%3D)

创建一个pygame.font.Font object对象

**fontObj = pygame.font.Font('freesansbold.ttf', 32)**#第一个参数为字体文件 第二个参数为字体大小

通过**render()**方法创建一个Surface对象 并将字写到上面

**textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)**#参数分别为 需要显示的字符串 是否抗锯齿 字体颜色 背景颜色

通过**get_rect()**属性创建一个width和height与Surface对象相同的rect对象

**textRectObj = textSurfaceObj.get_rect()**
通过设置rect对象的一个属性 来对rect的位置进行改变

**textRectObj.center = (200, 150)**
抗锯齿
抗锯齿会使得线条看起来平滑一些 看是会是程序变慢 **pygame.draw.aaline()**和
**pygame.draw.aalines()**都是抗锯齿的
# 音乐 #
看了下面的代码相信你会懂

	soundObj = pygame.mixer.Sound('beeps.wav')
	soundObj.play()
	import time
	time.sleep(1) # wait and let the sound play for 1 second
	soundObj.stop()
# pygame背景音乐 #

	# Loading and playing a sound effect:
	soundObj = pygame.mixer.Sound('beepingsound.wav')
	soundObj.play()
	# Loading and playing background music:
	pygame.mixer.music.load(backgroundmusic.mp3')
	pygame.mixer.music.play(-1, 0.0)
	# ...some more of your code goes here...
	pygame.mixer.music.stop()

**pygame.mixer.music.play(-1, 0.0)**函数的第一个参数表示背景音乐的循环次数 -1表示无限循环 第二个参数表示音乐开始的时间(s)