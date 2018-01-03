#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# IO编程--文件读写

#像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object
#第二个参数，'r'表示读，'w'表示写，'b'表示二进制，一般组合使用,例如；'rb','wb'
#第三个参数，表示该文件的字符编码

#一般情况下，Python解释器会将遇到的‘\’识别为路径，会自动增加一个'\'以便和转义字符进行区分，
#但若遇到转义字符则不增加‘\’。
filePath = 'E:/brave/PythonLearning/008_IO programming/text.txt'
f = open(filePath,'r',encoding='utf8')
try:
	f = open(filePath,'r',encoding='utf8')
	print(f.read())
finally:
	if f:
		f.close()

with open(filePath,'rb') as f:
	print(f.read())

# write的第二个参数如果是a表示追加（append）
with open(filePath,'a') as f:
	f.write('\nadd something...')