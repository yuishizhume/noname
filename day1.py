#大写字母A的编码是65，小写字母a的编码是97。

#输入输出
print 'The quick brown fox', 'jumps over', 'the lazy dog'
name = raw_input('Please enter your name:')
point = input('Please enter your point:')
print 'Hello',name,'Your point is:',point
#转义字符的使用方法
print r'\\\t\\'
print '''line1
line2
line3'''
#利用ASCII编码实现字母和对应数字转换
ord('A')
chr(65)
#Unicode
print u'中文'
u'中'
#Unicode与UTF-8互相转换
u'中文'.encode('utf-8')
'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
#格式化（与c一致，用%实现
#%d整数%f浮点数%s字符串%x十六进制整数
'Hi,%s,you have $%d.'%('Micheal',1000)
print u'你好啊，%s'%u'使用者'
#格式化还可以指定补0和取多少位%0（总位数.（小数点位数
'%08.3f'%3.1415926535897932254626

#list创建与增删改
classmates=['Jack','Bob','Adam']
classmates
len(classmates)
classmates[0],classmates[-1]=classmates[-1],classmates[0]
classmates
classmates.append('Micheal')
classmates
classmates.insert(2,'Cirra')
classmates
classmates.pop()
classmates.pop(2)
classmates[2]='Sarah'
classmates
#list元素也可以是其他数据类型或者又一个list
L=['Apple',123,True]
p=['asp','php']
s=['python','java',p,'scheme']
p[1]==s[2][1]

#tuple(不可变的list)
classmates=('Jack','Bob','Adam')
t=(1,)

#条件判断与循环
age=2
if age>=18:
    print 'your age is',age
    print 'adult'
elif age>=12:
    print 'your age is',age
    print 'teenager'
elif age>=6:
    print 'your age is',age
    print 'kid'
else:
    print 'your age is',age
    print 'baby'
names=['Macheal','Bob','Tracy']
for name in names:
    print name
sum=0
for x in range(10):#注意数字范围是小于10
    sum+=x
print sum
sum=0#计算100以内奇数和
n=99
while n>0:
    sum+=n;
    n=n-2;
print sum
birth=int(input('please enter your birth year:'))
if birth<2000:
    print'00前'
else:
    print'00后'

#使用dict和set

#dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']
d['Adam'] = 67
d['Adam']
d['Adam'] = 63
d['Adam']#一个key只对应一个value
'Thomas' in d#判断是否存在，否则访问会报错
d.get('Thomas')#返回None的时候Python的交互式命令行不显示结果。
d.get('Thomas', -1)
d.pop('Bob')#dict内部存放的顺序和key放入的顺序是没有关系的
d
#和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而增加；
#需要占用大量的内存，内存浪费多。
#而list相反：
#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#需要牢记的第一条就是dict的key必须是不可变对象。

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 1, 2, 2, 3, 3])
s
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2

#再议不可变对象
a = ['c', 'b', 'a']
a.sort()
a
a = 'abc'
b = a.replace('a', 'A')
a
b