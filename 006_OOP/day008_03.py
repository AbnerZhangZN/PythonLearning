#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# 面向对象编程-继承和多态

#“开闭”原则
#	对扩展开放：允许新增Animal子类；
#	对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

#静态语言 vs 动态语言
#对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型
#	或者它的子类，否则，将无法调用run()方法。

#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象
#	有一个run()方法就可以了
#动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
class Animal(object):
	def run(self):
		print('Animal is running...')
class Dog(Animal):
	def run(self):
		print('Dog is running...')

class Cat(Animal):
	pass

animal = Animal()
animal.run()

dog = Dog()
dog.run()