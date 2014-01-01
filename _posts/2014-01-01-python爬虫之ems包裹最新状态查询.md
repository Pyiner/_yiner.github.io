---
layout: default
title: Python爬虫之EMS包裹最新状态查询
---
最近在学用Python用爬虫 正好这两天在等新买的小米 所以就试着写个抓取EMS最新状态的脚本

	# -*- coding: utf-8 -*-
	import urllib,urllib2
	from bs4 import BeautifulSoup
	postdata=urllib.urlencode({
	    'wen':'ET000000000CS',#EMS单号
	    'Submit2':'EMS单号查询',
	    })
	req = urllib2.Request(
	    url = 'http://ems183.cn/ems.php',
	    data = postdata
	)
	result = urllib2.urlopen(req)
	soup = BeautifulSoup(result)
	i=soup.findAll('div',"mailnum_result_box")
	ii=i[0]
	iii=BeautifulSoup(str(ii))
	q=iii.findAll('td')
	qq=q[-3:]
	for qqq in qq:
	    print qqq.string