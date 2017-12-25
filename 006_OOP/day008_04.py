#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# 面向对象编程-获取对象信息

#使用type()
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
import types
def fn():
	pass

print(type(123) == int)
print(type('str') == str)
print(type(None) == None)
#types 模块中定义的常量
print(type(abs) == types.BuiltinFunctionType)

print(type(lambda x:x) == types.LambdaType)
print(type(fn) == types.FunctionType)
print(type((x for x in range(1,20))) == types.GeneratorType)

#使用isinstance()
class Animal(object):
	pass
class Dog(Animal):
	pass
class Husky(Dog):
	pass
a = Animal()
d = Dog()
h = Husky()
print(isinstance(h, Animal))
print(isinstance(h, Dog))
print(isinstance(h, Husky))
print(isinstance(d, Husky))
print(isinstance([1,2,3],(list,tuple)))
#使用dir() 
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr(),可以直接操作一个对象的状态
print(dir(None))
print(dir('str'))
print(dir(object))
class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 10)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
print(getattr(obj, 'z', 404))
