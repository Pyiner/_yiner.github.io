---
layout: default
title: 使用Python+ gevent 实现的小说下载工具
---
看小说的时候经常想找一些txt下到手机上看 但是找txt还是比较麻烦 有些网站需要登录才能下载

所以就自己写了一个下小说的工具

从 顶点小说网 下载 这个网站还算不错的 文章的错字比较少

工具是用Python写的 使用
**Gevent Beautiful urllib2**
抓一下页面 然后处理一下就可以了 运行脚本的时候第一个参数是相应文章的目录页

比如 抓取斗破苍穹


	小说抓取.py http://www.23us.com/html/0/298/


----------


	# -*- coding: utf-8 -*-
	from BeautifulSoup import BeautifulSoup
	import urllib2
	import sys
	import threading
	import Queue
	import gevent
	from time import sleep
	import gevent.monkey
	gevent.monkey.patch_all()
	 
	class Novel(object):
	    def __init__(self,word,index):
	        self.word = word
	        self.index = index
	        return
	    def __cmp__(self,other):
	        return cmp(self.index,other.index)
	 
	q = Queue.PriorityQueue()
	 
	def write1(url,title,index,q):
	    t=1
	    while t:
	        try:
	            f = urllib2.urlopen(url)
	            t=0
	        except:
	            gevent.sleep(0)
	    soup = BeautifulSoup(f.read().decode('gbk','ignore'))
	    str1='\n'+title+'\n'+str(soup.find('dd',id='contents'))
	    str1=str1.replace('<br />\n<br />','\n')
	    str1=str1.replace('<br />','\n')
	    str1=str1.replace('&nbsp;',' ')
	    str1=str1.replace('<dd id="contents">','')
	    str1=str1.replace('</dd>','')
	    q.put(Novel(str1,index))
	    print title
	 
	if __name__=='__main__':
	    url = str(sys.argv[1])
	    f = urllib2.urlopen(url)
	    soup = BeautifulSoup(f.read().decode('gbk','ignore'))
	    title = soup.title.string.split()[0]
	    body = soup.findAll('td')
	    str3=range(len(body))
	    threads = []
	    #print body.__len__()
	    for i in body:
	        try:
	            str2=url+i.a['href']
	            threads.append(gevent.spawn(write1,str2,str(i.a.string),body.index(i),q))
	        except:
	            pass
	    gevent.joinall(threads)
	    f=open(title+'.txt','wt')
	    sys.stdout = f
	    while not q.empty():
	        print q.get().word
	    f.close()