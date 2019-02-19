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