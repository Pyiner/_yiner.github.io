---
layout: default
title: Python Property
---
Python有个非常好的概念叫做属性(`property`), 它让面向对象编程变得更加简单. 想详细说Python的属性之前，我们先看看为什么它是那么重要。

一个简单的例子假设有一天你需要一个类来存储摄氏度. 它还将实现一个方法将摄氏度转换为华氏度。这样做的方法之一是这样的。

    class Celsius:
        def __init__(self, temperature = 0):
            self.temperature = temperature
    
        def to_fahrenheit(self):
            return (self.temperature * 1.8) + 32
            
像我们期望的那样，我们可以改变类的属性和操作温度。

    >>> # create new object
    >>> man = Celsius()
    >>> # set temperature
    >>> man.temperature = 37
    >>> # get temperature
    >>> man.temperature
    37
    >>> # get degrees Fahrenheit
    >>> man.to_fahrenheit()98.60000000000001

额外的小数位是因为Python内部的浮点数算法问题 (在Python解释器中尝试 1.1 + 2.2). 每次我们操作像`temperature`这样的属性，Python会去查找对象的 `__dict__ `字典。就像下面这样

    >>> man.__dict__
    {'temperature': 37}

因此，`man.temperature` 在内部就变成  `man.__dict__['temperature']`.现在，我们继续假设我们的类在客户中流行，他们在他们的程序中使用我们的类。他们在将我们的类应用于各种各样的场景。直到有一天，一个用户反馈给我们，不应该接收小于-273的摄氏度（-273.15是绝对零度）。他希望我们对这个值进行约束，为了满足用户的需求，我们将我们的类升级到1.01版本。

##使用 Getters 和 Setters##

一个显而易见的方法是我们隐藏`temperature`属性，将它私有化。而使用`getter`和`setter`接口来操作它，像下面这样。

    class Celsius:
        def __init__(self, temperature = 0):
            self.set_temperature(temperature)
    
        def to_fahrenheit(self):
            return (self.get_temperature() * 1.8) + 32
    
        # new update
        def get_temperature(self):
            return self._temperature
    
        def set_temperature(self, value):
            if value < -273:
                raise ValueError("Temperature below -273 is not possible")
            self._temperature = value
            
我们可以看到方法`get_temperature()` 和`set_temperature()` 的定义。 此外， `temperature`被替换成了`_temperature`. 在Python中，下划线在属性开头表示私有属性。

    >>> c = Celsius(-277)
    Traceback (most recent call last):...
    ValueError: Temperature below -273 is not possible
    
    >>> c = Celsius(37)>>> c.get_temperature()
    37
    >>> c.set_temperature(10)
    
    >>> c.set_temperature(-300)
    Traceback (most recent call last):...
    ValueError: Temperature below -273 is not possible

这次升级成功的增加了一个新的约束，我们不在接受小于273的值

但是，Python本身是不支持私有属性的，添加下划线的做法只是一种约定。语言本身不提供任何约束。

    >>> c._temperature = -300
    >>> c.get_temperature()
    -300

但是这不是重点。最大的问题是，对于上次的更新，我们的客户需要将他们的代码从
`obj.temperature`改为`obj.get_temperature()`和 `obj.temperature = val` 改为`obj.set_temperature(val)`. 
这样也许会对他们造成成千上万行代码的修改量。
总之，我们的更新不是向后兼容的。这需要`property`来帮忙。
##Property的威力##
pythonic的方法来处理这个问题是使用`property`.下面是具体的做法。

    class Celsius:
        def __init__(self, temperature = 0):
            self.temperature = temperature
    
        def to_fahrenheit(self):
            return (self.temperature * 1.8) + 32
    
        def get_temperature(self):
            print("Getting value")
            return self._temperature
    
        def set_temperature(self, value):
            if value < -273:
                raise ValueError("Temperature below -273 is not possible")
            print("Setting value")
            self._temperature = value
    
        temperature = property(get_temperature,set_temperature)
        
我们向`get_temperature()`和`get_temperature()`各添加了一个`print()`函数，来观察他们的执行情况。最后一行，我们创建一个`property`对象`temperature`. 

简而言之, `property` 连接`get_temperature`和`set_temperature`来负责成员属性访问(`temperature`). 任何代码想要取得`temperature`的值的时候，都会自动的调用`get_temperature()`代替`__dict__ `字典_中查找。

同样的，任何代码想给`temperature`赋值的时候都会自动调`用set_temperature()`.这个Python中一个非常cool的特性。让我们看看它的实际应用。

    >>> c = Celsius()
    Setting value

我们可以看到当我们创建一个对象的时候`set_temperature()`被调用.你能猜到这事为什么吗。原因是创建一个对象的时候，会调用初始化方法`__init__()`(最先调用的方法是`__new__()`). `__init__()`中有一行

`self.temperature = temperature`. 这个语句会自动调用`set_temperature().`
    
    >>> c.temperature
    Getting value
    0

同样的，像`c.temperature`这样的会自动调用`get_temperature()`. 
这就是`property`做的事情，我们来看更多的例子。

    >>> c.temperature = 37Setting value
    >>> c.to_fahrenheit()
    Getting value
    98.60000000000001

通过使用属性,我们可以看到,我们修改类和实现约束没有任何需要客户端代码的地方。因此我们的实现是向后兼容的,每个人都快乐。

最后注意,实际温度的值存储在私有变量`_temperature`中。属性`temperature`是一个为私有变量提供接口的`property`对象。

##深入 Property##

在Python中property()是一个内建函数，创建并返回一个property对象。函数的定义如下。

    property(fget=None, fset=None, fdel=None, doc=None)
    
`fget`是获取属性的值的函数,`fset`是设置属性值的函数,`fdel`是删除属性的函数,`doc`是一个字符串(like a comment).从实现来看，这些参数都是可选的，所以可以向下面这样简单的创建一个`property`对象。

    >>> property()
    <property object at 0x0000000003239B38>

`property`有三个方法`getter()`, `setter()`和`delete()` 来指定`fget`, `fset`和`fdel`。
这表示以下这行

    temperature = property(get_temperature,set_temperature)

可以被分解为

    # make empty property
    temperature = property()# assign fget
    temperature = temperature.getter(get_temperature)# assign fset
    temperature = temperature.setter(set_temperature)

这两块代码是等价的。
熟悉Python装饰器的可以发现，上面这种结构可以用装饰器来实现。我们可以不定义`get_temperature `和`set_temperature` 他们是不必要的，而且污染了类的命名空间。因此，我们重用`temperature`这个名字，当我们定义`getter`和`setter`的时候。这是可以做到的。

    class Celsius:
        def __init__(self, temperature = 0):
            self._temperature = temperature
    
        def to_fahrenheit(self):
            return (self.temperature * 1.8) + 32
    
        @property
        def temperature(self):
            print("Getting value")
            return self._temperature
    
        @temperature.setter
        def temperature(self, value):
            if value < -273:
                raise ValueError("Temperature below -273 is not possible")
            print("Setting value")
            self._temperature = value

上面的是实现`property`的简单而又被推荐的方法。在Python中寻找`property`的时候你很有可能遇到这种设计。


