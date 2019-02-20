# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 20:29:29 2019

@author: Administrator
"""
#高级特性
#掌握了Python的数据类型、语句和函数，基本上就可以编写出很多有用的程序了。
#构造一个1, 3, 5, 7, ..., 99的列表
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
#在Python中，代码不是越多越好，而是越少越好
#代码不是越复杂越好，而是越简单越好。

#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取前3个元素
r = []
n = 3
for i in range(n):
    r.append(L[i])
r
#这种操作用循环十分繁琐，因此可以使用切片（slice）操作符
L[0:3]#从索引0开始取，直到索引3为止，但不包括索引3
L[:3]#如果第一个索引是0，还可以省略
L[-2:]#['Bob', 'Jack']
L[-2:-1]#['Bob']
L = range(100)
L[:10]
L[-10:]
L[10:20]#前11-20个数
L[:10:2]#前10个数，每两个取一个
L[::5]#所有数，每5个取一个
L[:]#甚至什么都不写，只写[:]就可以原样复制一个list
#tuple也可以用切片操作
(0, 1, 2, 3, 4, 5)[:3]
#字符串
'ABCDEFG'[:3]
'ABCDEFG'[::2]

#迭代
#通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
#在Python中，迭代是通过for ... in来完成的
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
#默认情况下，dict迭代的是key。
#如果要迭代value，可以用for value in d.itervalues()
#如果要同时迭代key和value，可以用for k, v in d.iteritems()
for ch in 'ABC':
    print ch
#如何判断一个对象是可迭代对象呢？
#通过collections模块的Iterable类型判断
from collections import Iterable
isinstance('abc', Iterable)
isinstance([1,2,3], Iterable)
isinstance(123, Iterable)
#如何对list实现类似Java那样的下标循环
#Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print i, value
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y

#小结

#任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，
#只要符合迭代条件，就可以使用for循环。


#列表生成式
#列表生成式即List Comprehensions
#是Python内置的非常简单却强大的可以用来创建list的生成式
range(1, 11)
[x * x for x in range(1, 11)]
[x * x for x in range(1, 11) if x % 2 == 0]
#筛选出仅偶数的平方
#还可以使用两层循环，可以生成全排列
[m + n for m in 'ABC' for n in 'XYZ']
#三层和三层以上的循环就很少用到了。
import os # 导入os模块，模块的概念后面讲到
[d for d in os.listdir('.')] # os.listdir可以列出文件和目录
#for循环其实可以同时使用两个甚至多个变量
#比如dict的iteritems()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.iteritems():
    print k, '=', v
#因此，列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k + '=' + v for k, v in d.iteritems()]
#把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]


#小结
#运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。

#生成器
#受到内存限制，列表容量肯定是有限的
#如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了
#如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#这样就不必创建完整的list，从而节省大量的空间。
#在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。

#要创建一个generator，有很多种方法。
#把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]#list
g = (x * x for x in range(10))#generator
L,g#<generator object <genexpr> at 0x0000000009B992D0>
#怎么打印出generator的每一个元素呢？
#可以通过generator的next()方法
g.next()
#generator保存的是算法，每次调用next()，就计算出下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
#正确的方法是使用for循环
g = (x * x for x in range(10))
for n in g:
    print n
#基本上永远不会调用next()方法，而是通过for循环来迭代它。
#著名的斐波拉契数列（Fibonacci）
#除第一个和第二个数外，任意一个数都可由前两个数相加得到：
#1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
fib(6)
#要把fib函数变成generator，
#只需要把print b改为yield b就可以了：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
fib(6).next()#<generator object fib at 0x0000000009B99360>
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
#这里，最难理解的就是generator和函数的执行流程不一样。
#变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
#函数改成generator后，我们基本上从来不会用next()来调用它
#而是直接使用for循环来迭代：
for n in fib(6):
    print n
    
'''
小结：
generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。

要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。
'''
