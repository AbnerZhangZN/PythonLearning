#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#setup 11 函数-递归函数和尾递归函数
#递归函数
def fun(n): 
	if n==1:
		return 1
	return n * fun(n-1)
print(fun(1))
print(fun(5))
print(fun(100))
#print(fun(1000))
#尾递归 Python,Java都没有对尾递归进行优化，即使使用尾递归还是会出现栈内存溢出，C语言有对于尾递归的优化
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占
# 用一个栈帧，不会出现栈溢出的情况。
def funS(n):
	return funS_iter(n, 1)
def funS_iter(num, product):
	if(num==1):
		return product
	return funS_iter(num-1, num+product)

print(funS(100))
print(funS(1000))