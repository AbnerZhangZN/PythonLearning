#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#setup 12 高级特性-切片
#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
L=['Michael','Sarah','Jackie','Bob','Tracy','Kobe']
print([L[0],L[1],L[2]])
print(L[0:3])
print(L[:4])
print(L[1:4])
print(L[-1:])
T=('Michael','Sarah','Jackie','Bob','Tracy','Kobe')
print(T[0:3])
print(T[:4])
print(T[1:4])
#[::]两个“:”，可以将最后一个参数视作步长
L=list(range(100))
print(L)
print(L[:5])
print(L[0:10:2])
print(L[::3])
print(L[::-1])
print(L[::-2])
print(L[:-3])
print(L[len(L)-3:len(L)])

def trim(s):
	while s[:1]==' ':
		s = s[1:len(s)]
	while s[len(s)-1:len(s)]==' ':
		s = s[:len(s)-1]
	return s
print(trim('   asdf   '))
print(len(trim('   asds   ssf   ')))