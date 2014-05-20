---
layout: default
title: Python 的闭包
---
#Python 的闭包#

一个函数定义在另外一个函数内叫做内嵌函数, 内嵌函数可以访问外部作用域的变量. 在Python中, 这些非局部变量在默认的情况下是只读的.我们使用global来声明他们是非局部变量才能对他们进行修改.下面是一个内嵌函数访问非局部变量的例子.

    def print_msg(msg):
        """This is the outer enclosing function"""
    
        def printer():
            """This is the nested function"""
            print(msg)
    
        printer()
        
我们像下面这样执行这个函数.

    >>> print_msg("Hello")
    Hello

我们可以看到内嵌函数printer()可以访问外部函数的变量msg. 对于上面这个例如,如果我们让函数print_msg()返回函数the printer()而不是调用它,会反生生么呢？我们像下面这样重新定义函数.


    def print_msg(msg):
        """This is the outer enclosing function"""
    
        def printer():
            """This is the nested function"""
            print(msg)
    
        return printer  # this got changed

现在,让我们调用函数.
    
    >>> another = print_msg("Hello")
    >>> another()
    Hello
                                                                            
反常的,使用参数"Hello"调用函数print_msg()返回一个函数并把这个函数绑定到变量another上.调用another(),虽然print_msg()已经执行结束了，依然打印"Hello".将一些数据("Hello")添加到代码上,这个叫做Python的闭包.

这个值始终会被记住,即使超出范围,或者函数从当前命名空间中删除.

    >>> del print_msg
    >>> another()
    Hello
    >>> print_msg("Hello")
    Traceback (most recent call last):
    ...
    NameError: name 'print_msg' is not defined

我们再来看看,为什么这个值会一直存在.
printer将它所引用的外部对象msg添加到__closure__列表中.因为msg引用计
数增加了,所以就算print_msg堆栈帧没有了,msg对象也不会被回收。
    >>> printer.__closure___
    (<cell at 0x109e0aef8: str object at 0x109b925a8>,)


**我们什么时候会有闭包?**
从上面的例子我们可以看到,当一个内嵌函数引用其外部作用于中的变量,我们就会得到一个闭包.
总结一下,创建一个闭包必须满足以下几点:

1.必须有一个内嵌函数
2.内嵌函数必须引用外部函数中的变量
3.外部函数的返回值必须是内嵌函数

**什么时候使用闭包?**
那闭包又有什么用呢? 闭包可以避免使用全局变量,提供某某种形式的数据隐藏.它也可以为问题提供一个面向对象的解决办法.  当有几个方法（在大多数情况下,一个方法）将在类中实现，闭包可以提供替代和更优雅的解决方案。但是，当属性和方法的数量越来越大，更好的方法是实现一个类.

下面是一个简单的例子,定义一个闭包可能比定义一个类再创建一个函数要更方便.当然,具体如何做要看个人习惯.
    
    def make_multiplier_of(n):
        def multiplier(x):
            return x * n
        return multiplier

    >>> times3 = make_multiplier_of(3)
    >>> times5 = make_multiplier_of(5)
    
    >>> times3(9)
    27
    >>> times5(3)
    15
    >>> times5(times3(2))
    30
装饰器是闭包在Python中一种常见的使用方式.

所有函数都有一个名字叫做`__closure__`的属性, 它的值是一个cell对象的元组.参照上面的例子,我们知道times3和times5是闭包函数.
    
    >>> make_multiplier_of.__closure__
    >>> times3.__closure__
    (<cell at 0x0000000002D155B8: int object at 0x000000001E39B6E0>,)

cell对象有一个cell_contents的熟悉,存储了闭包变量的值
    
    >>> times3.__closure__[0].cell_contents
    3
    >>> times5.__closure__[0].cell_contents
    5

##"延迟获取"的闭包##
使用闭包，还需注意 "延迟获取" 现象。看下面的例子：

    >>> def test():
    ... for i in range(3):
    ... def a():
    ... print i
    ... yield a
    >>> a, b, c = test()
    70
    >>> a(), b(), c()
    2
    2
    2

为什么输出的都是2呢？
首先,`test`只是返回函数对象,并没有执行.其次, `test`完成`for`循环时,i已经等于2,所以执
行 `a b c` 时，它们所持有`i`自然也就等于2。
