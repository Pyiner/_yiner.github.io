---
layout: default
title: pyInstaller简明教程 （2013-5-2更新）
---
pyInstaller是一款用于将pyhon程序打包成exe文件的工具

pyInstaller不是一个python的包 只需要把pyInstaller的文件下载下来放到任意为止都可以

py2.6+ 需要pywin32的支持 下载地址http://www.lfd.uci.edu/~gohlke/
pythonlibs/2ibychs8/pywin32-218.win-amd64-py2.7.exe

然后在pyInstaller的目录下为py文件创建对应的spec文件

	pyinstaller.py C:\HelloWorld.py
未指定别的参数的话 会在pyinstaller的目录下 生成文件夹HelloWorld

**HelloWorld>dist**下面生成可执行文件**HelloWorld.exe**

HelloWorld文件夹下有文件HelloWorld.spec 对于简单的程序 上面的HelloWorld.exe 就足够了 对于复杂的程序 需要对spec进行操作
然后使用

	python pyinstaller.py [opts] HelloWorld.spec

-F, –onefile	产生一个文件用于部署 (参见XXXXX).

-D, –onedir	产生一个目录用于部署 (默认)

-K, –tk	在部署时包含 TCL/TK

-a, –ascii	不包含编码.在支持Unicode的python版本上默认包含所有的编码.

-d, –debug	产生debug版本的可执行文件

-w,–windowed,
–noconsole
使用Windows子系统执行.当程序启动的时候不会打开命令行(只对Windows有效)

-c,–nowindowed,
–console
使用控制台子系统执行(默认)(只对Windows有效)

-s,–strip	可执行文件和共享库将run through strip.注意Cygwin的strip往往使普通的win32 Dll无法使用.

-X, –upx	如果有UPX安装(执行Configure.py时检测),会压缩执行文件(Windows系统中的DLL也会)(参见note)

-o DIR, –out=DIR	指定spec文件的生成目录,如果没有指定,而且当前目录是

PyInstaller的根目录,会自动创建一个用于输出(spec和生成的可执行文件)的目录.如果没有指定,而当前目录不是PyInstaller的根目录,则会输出到当前的目录下.

-p DIR, –path=DIR	设置导入路径(和使用PYTHONPATH效果相似).可以用路径分割符(Windows使用分号,Linux使用冒号)分割,指定多个目录.也可以使用多个-p参数来设置多个导入路径

–icon=<FILE.ICO>	将file.ico添加为可执行文件的资源(只对Windows系统有效)
	
–icon=<FILE.EXE,N>	将file.exe的第n个图标添加为可执行文件的资源(只对Windows系统有效)
	
-v FILE, –version=FILE	将verfile作为可执行文件的版本资源(只对Windows系统有效)

然后创建exe文件

	pyinstaller.py C:\HelloWorld.spec

如果要在打包的程序中加入素材文件的话 需要对py代码 和spec文件中的代码进行修改

如果打包成一个exe文件的话 那么需要把py文件中获取文件的路径改为

	os.path.join(os.environ['_MEIPASS2'], 'cat.png')

然后在spec文件中

	a.binaries+[('cat.png','E:\\cat.png','DATA')] ,

早a.binaries后面加上一个三元组列表(名字，路径，‘DATA’)

如果打包成一个目录 那么需要把py文件中获取文件的路径改为

	os.path.join(os.path.dirname(sys.executable), 'cat.png'))

然后在spec文件中 在collect的a.binaries后面加上一个三元组列表**(名字,路径,’DATA’)**

添加数据文件的方法在某些机器上运行的时候会出现错误 以后如果找到解决办法会更新这篇文章的

更详细的信息可以查阅官方文档