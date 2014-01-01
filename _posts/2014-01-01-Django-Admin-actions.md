---
layout: default
title: Django Admin actions
---
使用一个函数对选中的条路做统一的改变。
三个参数：

- The current ModelAdmin
- An HttpRequest representing the current request,
- A QuerySet containing the set of objects selected by the user.


----------

	from django.db import models
	
	STATUS_CHOICES = (
	    ('d', 'Draft'),
	    ('p', 'Published'),
	    ('w', 'Withdrawn'),)
	
	class Article(models.Model):
	    title = models.CharField(max_length=100)
	    body = models.TextField()
	    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	
	    # On Python 3: def __str__(self):
	    def __unicode__(self):
	        return self.title
	from django.contrib import adminfrom myapp.models import Article
	
	def make_published(modeladmin, request, queryset):
	    queryset.update(status='p')make_published.short_description = "Mark selected stories as published"
	
	class ArticleAdmin(admin.ModelAdmin):
	    list_display = ['title', 'status']
	    ordering = ['title']
	    actions = [make_published]
	
	admin.site.register(Article, ArticleAdmin)      
  
但是因为actions和这个Admin是紧耦合的，所以我们把这个函数当做方法卸载Admin内部

    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='p')
    make_published.short_description = "Mark selected stories as published"

这里在actions中使用了字符串代替了上面的函数名，表示在make_published是方法。

使用self.message_user来对用户进行提示

使用action来提供一个中间页
直接返回一个响应

	from django.http import HttpResponsefrom django.core import serializers

	def export_as_json(modeladmin, request, queryset):
   		response = HttpResponse(content_type="application/json")
    	serializers.serialize("json", queryset, stream=response)
    	return response

或者重定向
	
	from django.contrib import admin
	from django.contrib.contenttypes.models import ContentType
	from django.http import HttpResponseRedirect

	def export_selected_objects(modeladmin, request, queryset):
	    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
	    ct = ContentType.objects.get_for_model(queryset.model)
	    return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))

将actions作用于全站,第二个参数是名字.

	admin.site.add_action(export_selected_objects, 'export_selected')
禁用actions

	admin.site.disable_action('delete_selected')#禁用了自带的删除
	admin.site.disable_action('delete_selected')                                                                                                       class SomeModelAdmin(admin.ModelAdmin):
	    actions = ['some_other_action']
	    ...
	
	class AnotherModelAdmin(admin.ModelAdmin):
	    actions = ['delete_selected', 'a_third_action']
	    ...

actuions只是ModelAdmin的一个字段,如果想禁用一个ModelAdmin的所有actions

	class MyModelAdmin(admin.ModelAdmin):
	    actions = None

如果想对用一个ModelAdmin下的不用字段或者同一字段对不用用户使用不同的actions,那么就覆盖掉get_actions方法.

返回一个允许的actions字典,keys是action的名字,value是一个(function,name,short_description)的元组.

	class MyModelAdmin(admin.ModelAdmin):
	    ...
	
	    def get_actions(self, request):
	        actions = super(MyModelAdmin, self).get_actions(request)
	        if request.user.username[0].upper() != 'J':
	            if 'delete_selected' in actions:
	                del actions['delete_selected']                                                                             return actions


