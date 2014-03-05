---
layout: default
title: 在BAE上用Django开发博客——视图
---
# 首页的view #

这里主要的问题就是一个分页，使用官方的分页函数可以轻松搞定，具体看代码

	from django.core.paginator import Paginator
	def Index(request):
	    num = request.GET.get('page')
	    if num:
	        num = int(num)
	    else:
	        num=1
	    article=Article.objects.all().order_by("-id")
	    p = Paginator(article, 5)#每5篇文章一页
	    page = p.page(num)
	    if num == p.num_pages:#找到了最后一页
	        pnum = None
	    else:
	        pnum = num+1
	    c = GetCategory()#获取分类列表
	    o = GetOpenProject()#获取开源项目列表
	    f = GetFriendUrl()#获取友情链接列表
	    return render_to_response('index.html',{'P':page,'Pnum':pnum,'C':c,'Open':o,'Friend':f})


在数据库里查询出的文章列表是从最早的往最晚的显示的，需要倒转过来，使用order_by来设置排序规则，其中‘-id’表示按id倒着输出
