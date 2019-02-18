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
