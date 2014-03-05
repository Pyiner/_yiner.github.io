---
layout: default
title: 在BAE上用Django开发博客——在BAE上部署
---
#在BAE上部署#

首先，把数据库上传到BAE，需要注意的是，对于Django App的名字中（我这里的Blog），如果有大写的话，导出的SQL文件中都变成小写的了，而如果上传到云数据库以后还是小写的话，BAE查询的时候会找不到，所以导出SQL以后需要手动替换下大小写。

本地工程和在BAE上部署的是有区别的。
首先，在项目的目录外头，多三个文件**app.conf**，**favicon.ico**，**index.py**

**app.conf**主要是用来控制后端WEB server的处理逻辑的。app.conf的作用比较多，其中主要的功能是实现URL rewrite。

	handlers:
	  - url : /static/(.*)
	    script : /static/$1
	  - url : /templates/(.*)
	    script : /templates/$1
	  - url : /.*
	    script : index.py
	  - expire : .jpg modify 10 years
	  - expire : .swf modify 10 years
	  - expire : .png modify 10 years
	  - expire : .gif modify 10 years
	  - expire : .JPG modify 10 years
	  - expire : .ico modify 10 years

关于app.conf的详细介绍请看：[http://godbae.duapp.com/?p=44#comment-12](http://godbae.duapp.com/?p=44#comment-12)

**favicon.ico**就是网站的favicon了。我后来在head标签里写了favicon，没用到这里这个。

**index.py**主要是Django相关配置的吧，这个我也说不好。里面的项目名，需要根据自己的改一下

	import os
	import sys
	
	os.environ['DJANGO_SETTINGS_MODULE'] = 'MyBlog.settings'
	
	path = os.path.dirname(os.path.abspath(__file__)) + '/MyBlog'
	if path not in sys.path:
	  sys.path.insert(1, path)
	
	from django.core.handlers.wsgi import WSGIHandler
	from bae.core.wsgi import WSGIApplication
	
	application = WSGIApplication(WSGIHandler())
