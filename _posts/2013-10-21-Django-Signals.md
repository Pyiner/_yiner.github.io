---
layout: default
title: Django Signals
---
Django的信号机制.

使用这个我们可以做很多事情,下面说说使用Signal在model save的时候做别的事情.

	from django.db.models.signals import post_save
	from django.dispatch import receiver
	
	@receiver(post_save, sender=Article)
	def article_out(sender,instance,**kwargs):
	    sender是发送信号的model
	    instance是当前修改的数据


post_save是指在model save之后调用函数,对应的还有pre_save.

使用这个把这个博客的文章备份从定时备份改到save一次 备份一次
