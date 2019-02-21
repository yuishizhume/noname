# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 09:52:41 2019

@author: Administrator
"""
#day4

#装饰器

#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print '2013-12-25'
f = now
f()
#函数对象有一个__name__属性，可以拿到函数的名字：
now.__name__
f.__name__
#现在，假设我们要增强now()函数的功能,但又不希望修改now()函数的定义
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
#观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
#我们要借助Python的@语法，把decorator置于函数的定义处
@log
def now():
    print '2013-12-25'
now()
#把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在
#只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数
#即在log()函数中返回的wrapper()函数。
#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
#在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
#写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print '2013-12-25'
now()
#和两层嵌套的decorator相比，3层嵌套的效果是这样的：
now = log('execute')(now)
#首先执行log('execute')，返回的是decorator函数，再调用返回的函数
#参数是now函数，返回值最终是wrapper函数。
'''以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是
对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的
__name__已经从原来的'now'变成了'wrapper'：'''
now.__name__#'wrapper'
#不需要编写wrapper.__name__ = func.__name__这样的代码
#Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
#或者针对带参数的decorator：
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
#import functools是导入functools模块。
#只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。
    
#小结
'''在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式
需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法
层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。
decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。'''


#偏函数
#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。
#通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。
#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
int('12345')
#但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
int('12345', base=8)#5349
int('12345', 16)#74565
#假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦
#于是，我们可以定义一个int2()的函数，默认把base=2传进去：
def int2(x, base=2):
    return int(x, base)
#这样，我们转换二进制就非常方便了：
int2('1000000')#64
int2('1010101')#85
#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()
#可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int, base=2)
int2('1000000')#64
#所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值）
#返回一个新的函数，调用这个新函数会更简单。
#注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
int2('1000000', base=10)#1000000
#最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
int2 = functools.partial(int, base=2)
#实际上固定了int()函数的关键字参数base，也就是：
#int2('10010')#相当于：
#kw = { base: 2 }
int('10010', **kw)
#当传入：
max2 = functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边，也就是：
max2(5, 6, 7)
#相当于：
args = (10, 5, 6, 7)
max(*args)#结果为10。

#小结
'''当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新
的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。'''
