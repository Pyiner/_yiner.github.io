---
layout: default
title: 使用xlrd模块 读取excel文件
---
首先导入模块

	from xlrd import open_workbook
然后创建文件对象

	wb = open_workbook(file,'rb')
	for s in wb.sheets():#遍历工作表
	s.cell(x,y)表示x行y列的元素 这里的元素不是str类型

在excel中 两个单元格之间相差一个Tab

只介绍了读取excel里面的文件 希望对大家的入门提供方便 更复杂的内容大家慢慢探索