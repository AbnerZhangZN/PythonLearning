#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# 面向对象高级编程-定制类

# __init__ 初始化方法
# __str__ 用于打印 __repr__
class Beauty(object):
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return 'Beauty object __str__ (name: %s)' %self.name
		
	def __repr__(self):
		return 'Beauty object __repr__ (name: %s)' %self.name
	
b = Beauty('Laury')
print(b)
b
#__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
#	也就是说，__repr__()是为调试服务的

#__iter__ 用于循环 __next__()也需要
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
	
	def __iter__(self):
		return self
		
	def __next__(self):
		self.a, self.b = self.b, self.a+self.b
		if self.a>1000:
			raise StopIteration()
		return self.a
		
for n in Fib():
	print(n)
	
#__getitem__ 实现func()[],例如list的第几个数，切片，或者是dict的key对应的value
#__setitem__ 对于集合list或dict来赋值
#__delitem__ 用于删除某个元素

#duck 类型

#__getattr__ 可动态调用类的方法和属性
class BeautyTmp(object):
	def __init__(self):
		self.name = 'Jackie'
		
	def __getattr__(self, attr):
		if attr == 'score':
			return 89
		if attr == 'get_age':
			return lambda :20
		raise AttributeError('object has no attribute %s'%attr)
	
	def __call__(self):
		print('My name is %s'%self.name)
		
bTmp = BeautyTmp()
print(bTmp.name)
print(bTmp.score)
print(bTmp.get_age())
print(bTmp())
print(callable(bTmp))
#__call__ 直接在实例本身调用
#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。


