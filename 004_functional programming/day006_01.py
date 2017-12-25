#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#setup 18 函数式编程-返回函数

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f=lazy_sum(1,3,5,7,9)
print(f)
print(f())

#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#def createCounter():
#	i = 0
#	def counter():
#		nonlocal i
#		i += 1
#		return i
#	return counter
def createCounter():
	i = 0
	return lambda:i+1

#def createCounter():
#	def counter(i):
#		def g():
#			return i+1
#		return g
#	fs = []
#	for j in range(1,10):
#		fs.append(counter(j))
#	return fs
counterA = createCounter()
print(counterA(),counterA(),counterA(),counterA(),counterA(),counterA())
counterB = createCounter()
print(counterB(),counterB(),counterB(),counterB())
