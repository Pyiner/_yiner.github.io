---
layout: default
title: Http Request Client —— Http请求发送工具
---
好久没更新博客了，上次还是上学期的时候，后来又要期末考试了，也没学什么新的东西，所以就没写啥。

假期的时候在家开发了一个情侣博客，差不多算是写完了，但是有些细节的地方没处理，放到的Bae上，等把细节处理好了再发出来。

然后看了几天Ajax，也没什么写什么东西，就是把博客的登录Ajax了一下，哈哈。

 
在开发和日常上网的过程中，经常需要发送Http请求，用requests这个库还是很方便的，但是每次都要去重新写代码，觉得是不那么方便，所以就写了**Http请求发送的工具**，主要是把requsts简单封装了下，主要是方便处理headers 和 post时候的data。直接复制chrome里面看到的请求内容就行。没显式的选择GET和POST方法，如果data里面的数据有意义就POST 不然就 GET。可以保存和载入方案，满足基础的要求。一些复杂的问题，还是得编码处理。

项目放到了Github上，算是我迈向开源的第一步吧~ 
[https://github.com/Yiner/](https://github.com/Yiner/ "https://github.com/Yiner/")

![](http://bcs.duapp.com/blog-pyiner/%E6%9C%AA%E5%91%BD%E5%90%8D.jpg?sign=MBO:528b10b38a1b368b5a572d8d459f541b:tHjXMhsGx5RW2TqxHHkBO%2Ftdpe4%3D)