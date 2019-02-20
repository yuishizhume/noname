# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:47:55 2019

@author: Administrator
"""
#day3


#函数式编程
#函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。
#函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
#Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

#高阶函数

#变量可以指向函数
#以Python内置的求绝对值的函数abs()为例，调用该函数用以下代码：
abs(-10)
#如果只写abs
abs#<function abs>
#可见，abs(-10)是函数调用，而abs是函数本身。
#如果一个变量指向了一个函数，那么，可否通过该变量来调用这个函数？
f = abs
f(-10)
#成功！说明变量f现在已经指向了abs函数本身。
#函数名也是变量
#函数名其实就是指向函数的变量,对于abs()这个函数，完全可以把函数名abs看成变量
#如果把abs指向其他对象，会有什么情况发生？
abs = 10
abs(-10)
#注：由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10。

#传入函数
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)
add(-5, 6, abs)

#map/reduce
#Python内建了map()和reduce()函数。
#map()函数接收两个参数，一个是函数，一个是序列
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
#一个函数f(x)=x²，要把这个函数作用在一个list[1, 2, 3, 4, 5, 6, 7, 8, 9]
def f(x):
    return x * x
map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数
#reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    return x + y
reduce(add, [1, 3, 5, 7, 9])#与sum同
def fn(x, y):
    return x * 10 + y
reduce(fn, [1, 3, 5, 7, 9])#13579
#考虑到字符串str也是一个序列，对上面的例子稍加改动
#配合map()，我们就可以写出把str转换为int的函数
def fn(x, y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
reduce(fn, map(char2num, '13579'))
#整理成一个str2int的函数就是：
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
#还可以用lambda函数进一步简化成：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))

#filter
#Python内建的filter()函数用于过滤序列。
#和map()类似，filter()也接收一个函数和一个序列。
#和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#在一个list中，删掉偶数，只保留奇数，可以这么写
def is_odd(n):
    return n % 2 == 1
filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
#把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()
filter(not_empty, ['A', '', 'B', None, 'C', '  '])
#可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。

#sorted
#Python内置的sorted()函数就可以对list进行排序：
sorted([36, 5, 12, 9, 21])
#此外，sorted()函数也是一个高阶函数
#如果要倒序排序，我们就可以自定义一个reversed_cmp函数：
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
sorted([36, 5, 12, 9, 21], reversed_cmp)
#再看一个字符串排序的例子：
sorted(['bob', 'about', 'Zoo', 'Credit'])
#按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
#尝试定义出忽略大小写的比较算法
def cmp_ignore_case(s1, s2):#实际上就是先把字符串都变成大写（或者都变成小写），再比较。
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

#返回函数
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
#我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
#但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数！
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(1, 3, 5, 7, 9)
f
f()#调用函数f时，才真正计算求和的结果
'''在这个例子中，我们在函数lazy_sum中又定义了函数sum，
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部
变量，当lazy_sum返回函数sum时，相关参数和变量都保存在
返回的函数中，这种称为“闭包（Closure）”的程序结构拥有
极大的威力。'''
#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
f1==f2
#f1()和f2()的调用结果互不影响。

#闭包
'''注意到返回的函数在其定义内部引用了局部变量args，所以，
当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
，所以，闭包用起来简单，实现起来可不容易。'''
#另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
#在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
#你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
#>>> f1()
#9
#>>> f2()
#9
#>>> f3()
#9
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个
#函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#如果一定要引用循环变量怎么办？方法是再创建一个函数
#用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
     fs = []
     for i in range(1, 4):
         def f(j):
             def g():
                 return j*j
             return g
         fs.append(f(i))
     return fs
f1, f2, f3 = count()
f1()
f2()
f3()
#缺点是代码较长，可利用lambda函数缩短代码。

#匿名函数
#当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
#在Python中，对匿名函数提供了有限支持。还是以map()函数为例
#计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数
map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#通过对比可以看出，匿名函数lambda x: x * x实际上就是：
def f(x):
    return x * x
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
#此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
f
f(5)
#同样，也可以把匿名函数作为返回值返回，比如
def build(x, y):
    return lambda: x * x + y * y
#小结
#Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。