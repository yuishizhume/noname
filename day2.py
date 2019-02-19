# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:28:47 2019

@author: Administrator
"""
#大写字母A的编码是65，小写字母a的编码是97。
#day2

#函数
#http://docs.python.org/2/library/functions.html#abs
#上面是python的内置函数
help(abs)
#也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。
abs(-12.34)
#abs(1, 2)#会报错并明确地告诉你原因
#数据类型转换
cmp(1, 2)#<-1=0>1
int('123')
float('12.34')
unicode(100)
bool(1)

#定义函数
#定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
my_abs(-12.34)
#空函数
def nop():
    pass#pass可以用来作为占位符
#现在还没想好怎么写函数的代码，就可以先放一个pass
#定义的my_abs没有参数检查，所以，这个函数定义不够完善。
#修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance实现
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
my_abs('123')
#返回多个值
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print x, y#返回值是一个tuple！

#函数的参数
def power(x, n=2):#计算x的n次方，默认平方
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
power(5, 3)
#有些参数不是默认，但是函数需要完整
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city#将年龄城市设为默认参数
enroll('Sarah', 'F')
enroll('Bob', 'M', 7)#按顺序提供默认参数
enroll('Adam', 'M', city='Tianjin')#参数用传进去的值，其他默认参数继续使用默认值。
#默认参数有个最大的坑
def add_end(L=[]):
    L.append('END')
    return L
add_end([1, 2, 3])
add_end()
add_end()#默认参数必须指向不变对象！
#可变参数
def calc(numbers):#参数个数不确定
    sum = 0#计算a²加b²加。。。
    for n in numbers:
        sum = sum + n * n
    return sum
calc([1, 2, 3])#先组装一个list或tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1, 2)
calc()
nums = [1, 2, 3]
calc(*nums)#加一个*号，把list或tuple的元素变成可变参数

#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数
#这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
#函数person除了必选参数name和age外，还接受关键字参数kw
person('Michael', 30)
person('Bob', 35, city='Beijing')
#也可以传人任意个数的关键字参数
person('Adam', 45, gender='M', job='Engineer')
#也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
#也可以简化
person('Jack', 24, **kw)

#参数组合
#可以用必选参数、默认参数、可变参数和关键字参数
#4种参数都可以一起使用
#请注意，参数定义的顺序必须是必选参数、默认参数、可变参数和关键字参数。
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1, 2, 3, 'a', 'b', x=99)
#通过一个tuple和dict，你也可以调用该函数
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)


#小结
'''
默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
'''

#递归函数
#一个函数在内部调用自身本身，这个函数就是递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)#计算阶乘n!
fact(100)
#fact(1000)#会溢出
#上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式
#所以就不是尾递归了。要改成尾递归方式，需要多一点代码
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
fact(1000)
#遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
