#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#setup 13 高级特性-迭代

#dict
d = {'a':1,'b':2,'c':3, 'd':4}
print('key迭代')
for key in d:
	print(key)

print('value迭代')
for value in d.values():
	print(value)

print('key,value迭代')
for k,v in d.items():
	print(k, ':', v)

for ch in 'Jackie':
	print(ch)

from collections import Iterable
print(isinstance('abc',Iterable))#str是否可迭代
print(isinstance([1,2,3],Iterable))#list是否可迭代
print(isinstance((1,2,3),Iterable))#tuble是否可迭代
print(isinstance(123,Iterable))#整数是否可迭代

#enumerate函数可以把一个list变成索引-元素对
for i,value in enumerate(['a','b','c']):
	print(i, value)
	
def findMinAndMax(L):
	min = None
	max = None
	for x in L:
		#print('ddd')
		if not min:
			min = x
		if not max:
			max = x
		#print('ddd2')
		if min > x:
			min = x
		if max < x:
			max = x
	return (min, max)
print(findMinAndMax([1,2,3,6]))