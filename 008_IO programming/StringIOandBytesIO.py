#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# IO编程--StringIO和BytesIO

#StringIO在内存中读写str,getvalue()方法用于获得写入后的str
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

#BytesIO操作的是二进制数据
from io import BytesIO
b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())