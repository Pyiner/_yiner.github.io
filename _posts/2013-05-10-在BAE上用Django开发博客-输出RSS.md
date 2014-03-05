---
layout: default
title: 在BAE上用Django开发博客——输出RSS
---
#输出RSS#

Django自带了RSS输出，用起来还是比较简单的。
首先在url中

	from Blog.MyFeed import LatestEntriesFeed
	urlpatterns = patterns('',
    		url(r'^feed$', LatestEntriesFeed()),
			)
然后在Blog目录下新建一个MyFeed的文件，具体代码如下：
	
	from django.contrib.syndication.views import Feed
	from Blog.models import Article
	import markdown
	
	class LatestEntriesFeed(Feed):
	    title = "Yiner in Python"
	    link = "http://www.pyiner.com/"
	    description = "Yiner in Python"
	    def items(self):
	        return Article.objects.order_by('-id')
	
	    def item_title(self, item):
	        return item.title
	
	    def item_description(self, item):
	        return markdown.markdown(item.content)
	
	    def item_link(self, item):
	         return self.link+item.url+'/'

items是获取的文章列表，item指一篇文章。

这里没有使用模版，所以使用markdown对item.content进行转义。

官方文档：[https://docs.djangoproject.com/en/dev/ref/contrib/syndication/](https://docs.djangoproject.com/en/dev/ref/contrib/syndication/)