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
'''
任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，
只要符合迭代条件，就可以使用for循环。
'''