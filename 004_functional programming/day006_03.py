#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#setup 20 函数式编程-装饰器

#假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
#但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def log(func):
	def wrapper(*args,**kw):
		print('call %s():'%func.__name__)
		return func(*args,**kw)
	return wrapper
@log
def now():
	print('2017/12/20')
	
now()

def log1(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print(text,'%s():'%func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator
@log1('execute')
def now():
	print('2017/12/20;aaa')
now()
	
def metric(fn):
	def wrapper(*args,**kw):
		print('%s executed in %s ms' % (fn.__name__, 10.24))
		return fn(*args,**kw)
	return wrapper
@metric
def now():
	print('111')
now()