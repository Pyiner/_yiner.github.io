---
layout: default
title: node-webkit开发初探 
---
node-webkit是一个基于Chromium 和 node.js的应用。
基于node-webkit 我们可以使用HTML Javascript 甚至是Nodejs来开发桌面应用。



因为学校教务处的成绩查询系统只支持IE，用起来比较麻烦，所以就做一个jwc成绩查询的客户端作为node-webkit的练习。

----------

项目的整体结构：
	
	├── node_modules
	│   └── iconv-lite
	├── index.html
	└── package.json

----------

package.json 是项目的配置文件，是必不可少的一部分

	{
	  "name": "node-webkit demo",//名字
	  "description": "this is about node-webkit demo",//描述
	  "version": "0.0.1",//版本号
	  "main": "index.html",//初始页面
	  "window": {
	  	"title": "webkit demo",//标题
	    "icon": "pub/images/favicon.ico",//icon路径
		"frame":true, //是否有外边框
		"toolbar":true //是否含有工具栏
	  }
	}

[更多关于package.json的信息](https://github.com/rogerwang/node-webkit/wiki/Manifest-format)

----------
首先，要解决登陆的问题
![](http://bcs.duapp.com/blog-pyiner/jwcloginpage.jpg?sign=MBO:528b10b38a1b368b5a572d8d459f541b:sh455vNpd1Hkm%2BXgdOsWOeyGJEw%3D)
登陆页面如上图所示，如果只有用户名和密码，那这个问题就很好解决，但是这里多出个了验证码就笔记比较麻烦了。

通过chrome查看登陆时候的HTTP请求内容，可以知道服务器记录了请求验证码的cookie，然后我们再通过使用同样的cookie来发送POST请求{用户名，密码，验证码}来登陆。

那么第一步就是请求验证码，记录服务器response header里的set-cookie值

	var fs = require("fs");
	var http = require("http");
	var url = "http://jwc.nenu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS";
	var file = fs.createWriteStream('num.jpg');//打开一个文件
	var cookies = null
	http.get(url,function(res){
	    res.on('data',function(data){
	        file.write(data)//讲图片内容写入文件
	        $('<img src="num.jpg">').insertAfter('#num');//插入img标签到DOM中
	        cookies = res.headers['set-cookie'][0].split(';')[0]//保存set-cookie的值
	    })
	})

在上面的代码中，我们请求到了验证码，并将验证码图片写入到本地文件中，然后记录了set-cookie的值。

**为什么我们要在代码里插入img标签，而不是直接将img标签写在html里呢？**
因为HTML页面的加载会先于代码执行结束，在渲染img标签的时候我们num.jpg还没有被写入到文件中。

----------

接下来我们就需要发送POST请求来登陆了

	var sclnum = $(".scl-num").val();
	var password = $(".password").val();
	var num = $(".num").val();
	var qs=require('querystring');
	var data = {WebUserNO:sclnum,Password:password,Agnomen:num}
	var content = qs.stringify(data)//将POST data 压缩
	var options = {
	    hostname: 'jwc.nenu.edu.cn',
	    port: 80,
	    path: '/ACTIONLOGON.APPPROCESS?mode=4',
	    method: 'POST',
	    headers:{//按照正常登陆时请求header的信息来设置，可以不设置这么多
	        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	        'Accept-Encoding':'gzip,deflate,sdch',
	        'Accept-Language':'zh-CN,zh;q=0.8',
	        'Cache-Control':'max-age=0',
	        'Connection':'keep-alive',
	        'Content-Length':content.length,//正文长度
	        'Content-Type':'application/x-www-form-urlencoded',
	        'Cookie':cookies,//携带请求验证码时的cookie
	        'Host':'jwc.nenu.edu.cn',
	        'Origin':'http://jwc.nenu.edu.cn',
	        'Referer':'http://jwc.nenu.edu.cn/ACTIONLOGON.APPPROCESS?mode=3'
	    }
	}
	var req = http.request(options,function(res){
	    //console.log(res);
	    res.setEncoding('utf8')
	    res.on('data',function(data){
	       });
	    });
	req.write(content)//在这里写入请求正文
	req.end()//必须要有请求结束，不然会报错

----------

登陆以后就可以携带上面的cookie直接访问我们需要的页面了

	var options2 = {
	    hostname: 'jwc.nenu.edu.cn',
	    port: 80,
	    path: 'http://jwc.nenu.edu.cn/ACTIONQUERYSTUDENTSCORE.APPPROCESS',
	    method: 'GET',
	    headers:{
	        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	        'Accept-Encoding':'gzip,deflate,sdch',
	        'Accept-Language':'zh-CN,zh;q=0.8',
	        'Cache-Control':'max-age=0',
	        'Content-Type':'application/x-www-form-urlencoded',
	        'Cookie':cookies,
	    }
	}
	var iconv = require('iconv-lite')
	var req2 =http.request(options2,function(res){
	    res.on('data',function(data){
	    	$('#login').hide();
	        $('#chengji').append($(iconv.decode(data,'gbk'),'[border=1]'));
	    })
	});
	req2.end();	

上面这段代码放在登陆代码的res.on内部的

    res.on('data',function(data){
		//请求页面代码
       });

**对于非utf-8编码的页面要怎么处理呢？**

上面我们请求的页面是gbk编码，nodejs本身是不支持gbk的，我们需要额外的库来处理。
iconv-lite 是iconv的轻量包，iconv-lite不需要编译，直接可以使用。

	var iconv = require('iconv-lite')
	iconv.decode(data,'gbk')//将gbk的buffer转化为字符串


这个项目勉强能用了，但是还是有有多地方要继续开发，逐渐进行完善。