#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# IO编程--操作文件和目录

#os 模块
import os
print(os.name)
#os.uname()只在类unix系统有用

#环境变量
print(os.environ)
print(os.environ.get('PATH'))

#操作文件和目录
print(os.path.abspath('.'))#当前文件路径
os.path.join('E:\\brave\\PythonLearning\\008_IO programming','testdir')
#os.mkdir('E:\\brave\\PythonLearning\\008_IO programming\\testdir1')
#os.rmdir('E:\\brave\\PythonLearning\\008_IO programming\\testdir1')

#os.path.join() 将两个路径合成一个
#os.path.split() 可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
#os.path.splitext()可以直接让你得到文件扩展名

print([x for x in os.listdir('.') if os.path.isdir(x)])

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])