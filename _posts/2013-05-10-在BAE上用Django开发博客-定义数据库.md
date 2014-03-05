---
layout: default
title: 在BAE上用Django开发博客——定义数据库
---
之前博客用的WordPress，早就想自己写一个了，一直没开始写，最近这几天把博客写完了，用的Django，放到了BAE上。

下面通过几篇博客介绍一下这个博客的开发。

# 定义数据库 #

首先，明确需要在数据库里存放哪些内容，我是models里是这样写的：

	from django.db import models
	from django.contrib import admin
	
	
	class Article(models.Model):#文章
	    title = models.CharField(max_length=64)#标题
	    url = models.CharField(max_length=64)#路径
	    date = models.DateTimeField()#时间
	    content = models.TextField()#正文
	    summary = models.TextField()#摘要
	    category = models.ForeignKey('Category')#分类
	    label = models.ManyToManyField('Label')#标签
	    num = models.IntegerField(default=0)#访问数
	    def __unicode__(self):
	        return self.title
	
	
	class Label(models.Model):
	    name = models.CharField(max_length=30)
	    def __unicode__(self):
	        return self.name
	
	class Category(models.Model):
	    name = models.CharField(max_length=30)
	    def __unicode__(self):
	        return self.name
	
	
	class OpenProject(models.Model):
	    name = models.CharField(max_length=30)
	    url = models.URLField()
	    def __unicode__(self):
	        return self.name
	
	
	class FriendUrl(models.Model):
	    name = models.CharField(max_length=30)
	    url = models.URLField()
	    def __unicode__(self):
	        return self.name
	
	
	class ArticleAdmin(admin.ModelAdmin):
	    list_display = ('title','date','url')
	
	
	class LabelAdmin(admin.ModelAdmin):
	    list_display = ('name',)
	
	class CategoryAdmin(admin.ModelAdmin):
	    list_display = ('name',)
	
	class OpenProjectAdmin(admin.ModelAdmin):
	    list_display = ('name',)
	
	class FriendUrlAdmin(admin.ModelAdmin):
	    list_display = ('name',)
	
	admin.site.register(Article,ArticleAdmin)
	admin.site.register(Label,LabelAdmin)
	admin.site.register(Category,CategoryAdmin)
	admin.site.register(OpenProject,OpenProjectAdmin)
	admin.site.register(FriendUrl,FriendUrlAdmin)


后台直接用的Django的Admin 

在**Article**里，因为url想用title以方便SEO，但是title中难免会有空格，而**url中是不能有空格的**，所以在写文章的时候自己添加一遍url，把空格替换成‘-’，这样写减少了views里处理程序的复杂度

**summary**摘要没有在后台截取，而是自己添加，这样可控性更强些。