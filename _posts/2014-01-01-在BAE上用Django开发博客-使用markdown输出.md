---
layout: default
title: 在BAE上用Django开发博客——使用markdown输出
---
#使用markdown来输出文章#

对于文章的编写，我使用的是markdown语法，先在本地用MarkdownPad编辑完以后，复制到后台，然后在模版输出的时候使用markdown过滤

首先，需要在**INSTALLED_APPS**里添加

	'django.contrib.markup'

然后在每一个用到markdown过滤的模版上加入

	{% load markup %}

具体过滤的时候：

	{{ markdown_content_var|markdown }}

我在上传到BAE以后， **{{ markdown_content_var|markdown}}**报错了，原因是我在管道‘|’两边加入了多余的空格