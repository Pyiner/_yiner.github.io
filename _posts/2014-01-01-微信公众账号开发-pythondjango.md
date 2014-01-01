---
layout: default
title: 微信公众账号开发实录——python+django
---
**最近微信很火啊~** 我也凑了个热闹 去弄了个公众账号 花了几个小时的时间让微信和百度开发者平台连通了 。

下面说一下我是怎么弄的吧 首先，注册一个账号。。。我相信这些大家都会的，我们从开发者认证开始说。

# 开发者认证： #

这里需要一个url 和一个token url就是微信和你交流的地址。token是一个自定义的字符串，用于验证什么的，暂时先不考虑。

认证的时候微信会往这个网址上通过get发送4个参数 型如

	http://www.baidu.com/signature=123&timestamp=123&nonce=123&echostr=123

要求再验证是微信发的以后 返回echostr参数的值 我在认证的时候没做验证 就直接返回的echoste的值
django代码如下： 

        echostr = request.GET['echostr']
	return HttpResponse(echostr)

# 接收和返回信息 #

微信通过post发送xml格式的信息

我们通过request.raw_post_data获取这个xml的字符串然后进行相应的处理，返回一个xml具体部分官方文档里有说,


	def Weixin(request):
	    if request.method=='POST':
	        from BeautifulSoup import BeautifulSoup
	        soup = BeautifulSoup(request.raw_post_data)
	        s="""<xml>
	             <ToUserName>"""+soup.fromusername.text+"""</ToUserName>
	             <FromUserName>"""+soup.tousername.text+"""</FromUserName>
	             <CreateTime>12345678</CreateTime> <MsgType>text</MsgType>
	             <Content>nihao</Content>
	             <FuncFlag>0</FuncFlag> </xml>"""
	    return HttpResponse(s)

这里需要注意的问题就是发过来xml档的标签名都是小写，和文档里说的不一样，所以才有soup.fromusername.text而不是soup.FromUserName.text