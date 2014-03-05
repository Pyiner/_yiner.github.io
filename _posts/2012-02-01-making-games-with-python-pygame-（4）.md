---
layout: default
title: Making Games with Python & Pygame （4）
---
所谓的动画简单来说就是根据时间的推移画面进行变化的效果

	import pygame, sys
	from pygame.locals import *
	
	pygame.init()
	
	FPS = 30 # frames per second setting
	fpsClock = pygame.time.Clock()
	
	# set up the window
	DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
	pygame.display.set_caption('Animation')
	
	WHITE = (255, 255, 255)
	catImg = pygame.image.load('cat.png')
	catx = 10
	caty = 10
	direction = 'right'
	
	while True: # the main game loop
	    DISPLAYSURF.fill(WHITE)
	
	    if direction == 'right':
	        catx += 5
	        if catx == 280:
	            direction = 'down'
	    elif direction == 'down':
	        caty += 5
	        if caty == 220:
	            direction = 'left'
	    elif direction == 'left':
	        catx -= 5
	        if catx == 10:
	            direction = 'up'
	    elif direction == 'up':
	        caty -= 5
	        if caty == 10:
	            direction = 'right'
	
	    DISPLAYSURF.blit(catImg, (catx, caty))
	
	    for event in pygame.event.get():
	        if event.type == QUIT:
	            pygame.quit()
	            sys.exit()
	
	    pygame.display.update()
	    fpsClock.tick(FPS)

![](http://bcs.duapp.com/blog-pyiner/RQBCUWYBHKQ0%40K5.jpg?sign=MBO:528b10b38a1b368b5a572d8d459f541b:Jny9tm64s2RcFRdvnCLKy3jWVwU%3D)
# 帧数和pygame.time.Clock对象 #

帧数就是画面数 FPS表示每秒的帧数 在Pygame程序中 FPS大小取决于每次绘制画面的复杂程度 

如果需要绘制的东西很多 每一帧需要的时间会很长 FPS会减小

如果画面需要绘制的东西比较少 那么每一帧的时间就会比较短 FPS会增加

为了不让我们的程序在绘制比较少的东西时运行速度过快 所以我们需要使用

pygame.time.Clock()创建一个pygame.time.clock对象

	fpsClock = pygame.time.Clock()

然后通过对象的tick()方法设置最大的FPS值

	fpsClock.tick(FPS)
**tick()**方法会自动计算上次运行这个方法到现在的时间 当这个时间达到所设定的值的时候 tick()方法才会被执行

所以将**fpsClock.tick(FPS)**放在**pygame.display.update()**之后就可以

**pygame.image.load()**函数和blit()方法

**pygame.image.load()**使用一个图片作为参数 返回一个Surface对象

**blit()**是Surface对象的是一个方法 参数为一个Surface对象 和一个坐标 这个坐标是前一个Surface内部的坐标

**DISPLAYSURF.blit(catImg, (catx, caty))** 将catImg绘制到DISPLAYURF上坐标为(catx,caty)的位置
