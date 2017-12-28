#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# 面向对象高级编程-多重继承

class Animal(object):
	pass

class Mammal(Animal):
	pass
	
class Bird(Animal):
	pass
	
class RunnableMixIn(object):
	def run(self):
		print('Running ....')
	
class FlyableMixIn(object):
	def fly(self):
		print('Flying ....')

#多重继承 MixIn 更多时候表示一个功能		
class Dog(Mammal,RunnableMixIn):
	pass
	
class Bat(Bird,FlyableMixIn):
	pass
	
dog = Dog()
dog.run()	
	