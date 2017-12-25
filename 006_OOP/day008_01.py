#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# 面向对象编程-类和实例

#类是抽象的模板, 实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同
#初始化方法__init__，第一个参数是self,表示创建的实例本身
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	
	def get_grade(self):
		if self.score >= 80:
			return 'A'
		elif self.score >= 70:
			return 'B'
		elif self.score >= 60:
			return 'C'
		else:
			return 'D'
			
lisa = Student('Lisa',85)
bob = Student('Bob',72)
print(lisa.name, lisa.get_grade())
print(bob.name, bob.get_grade())
lisa.age = 22
print(lisa.age)