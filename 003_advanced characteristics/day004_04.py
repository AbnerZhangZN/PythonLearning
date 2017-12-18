#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#setup 16 高级特性-迭代器

#1、集合数据类型 list tuple dict set str
#2、generator, 生成器和带yield的generator function

#使用isinstance()判断一个对象是否是Iterable对象：
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100, Iterable))

#使用isinstance()判断一个对象是否是Iterator对象：
#被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator))
print(isinstance({}, Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance('adc', Iterator))
print(isinstance(iter('adc'), Iterator))

#Iterable对象存储的是数据，Iterator对象存储的是得到数据的方法
#Iterable对象类似于把所有的自然数全部列出来，Iterator告诉你怎么把所有的自然数列出来