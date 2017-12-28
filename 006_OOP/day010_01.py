#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# 面向对象高级编程-使用@property 装饰器

#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查
#定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
class Student(object):
	
	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value

s = Student()
s.score = 23


class Screen(object):
	
	def check(value):
		def decorator(func):
			def wrapper(*args, **kw):
				if not isinstance(value, int):
					raise ValueError('value must be an integer!')
				return func(*args, **kw)
			return wrapper
		return decorator
	
	@property
	def width(self):
		return self._width
		
	@property
	def height(self):
		return self._height
		
	#@check(value)
	@width.setter
	def width(self, value):
		self._width = value
	
	#@check(value)
	@height.setter
	def height(self, value):
		self._height = value
	
	@property
	def resolution(self):
		return self._width * self.height
	
	
	
screen = Screen()
screen.width = 1024
screen.height = 768

print('resolution=', screen.resolution)