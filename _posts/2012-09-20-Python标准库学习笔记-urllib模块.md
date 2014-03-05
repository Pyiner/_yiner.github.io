---
layout: default
title: python标准库学习笔记 urllib模块
---
利用缓存实现简单的获取

	import urllib
	import os
	
	def reporthook(blocks_read,block_size,total_size):
	    if not blocks_read:
	        print 'Connection opened'
	        return
	    if total_size < 0:
	        print 'Read %d blocks ( %d bytes ) '%(blocks_read,blocks_read*block_size)
	    else:
	        amount_read = blocks_read*block_size
	        print 'Read %d blocks,or %d / %d'%\
	        (blocks_read,amount_read,total_size)
	
	try:
	    filename,msg = urllib.urlretrieve('http://zt.xiaomi.com/bbszt/rom/miuiv4_ics7.0/miuiV4_Mioneplus_ICS7.0_4.0_fastboot_dj8428bjkq.exe',
	    reporthook=reporthook)
	
	    print 
	    print 'File:',filename
	    print 'Headers'
	    print msg
	    print 'File exists before cheanup',os.path.exists(filename)
	
	finally:
	    #urllib.urlcleanup()
	
	    print ' File still exists:', os.path.exists(filename)

参数编码：

	import urllib
	
	query_args = {'q':'query string','foo':'bar'}
	
	encoded_args = urllib.urlencode(query_args)
	
	print 'Encoded:',encoded_args 
	
	query_args = {'q':['query string','bar']}
	
	print urllib.urlencode(query_args,doseq=True)#同一个名称与多个值关联 doseq = True	

路径与URL转换

	import os
	
	from urllib import pathname2url,url2pathname
	
	print '== Windows =='
	path = r'\a\b\c'#不包含驱动器字母
	print 'Original:',path
	print 'URL     :',pathname2url(path)
	print 'Path    :',url2pathname('/d/e/f')
	
	print 
	
	path = r'C:\a\b\c'#包含驱动器字母
	print 'Original:',path
	print 'URL     :',pathname2url(path)