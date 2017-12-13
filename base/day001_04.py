#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#setup 4 练习-字符串和编码
print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
print('中国话'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe5\x9b\xbd\xe8\xaf\x9d'.decode('utf-8'))
print(b'ABC'.decode('ascii'))
print(b'ABC'.decode('utf-8'))

print(len('ABC'))#3
print(len('中文'))#2
print(len(b'ABC'))#3
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))#6
print(len('中文'.encode('utf-8')))#6

#格式化
#%d	整数
#%f	浮点数
#%s	字符串
#%x	十六进制整数
print('格式化')
print('%2d-%02d' % (3,1))
print('%.2f' % 3.1415926)
print('Hello, %s ,you own me $%d!'%('Jack',10000))
#format()
print('{0},你成绩下降了{1:.3f}%'.format('小明',3.1415926))