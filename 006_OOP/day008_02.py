#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# 面向对象编程-访问控制

# Python本身没有任何机制阻止你干坏事，一切全靠自觉
#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
#在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
	def __init__(self, name, gender):
		self.__name = name
		self.__gender = gender
	
	def get_grade(self):
		if self.__score >= 80:
			return 'A'
		elif self.__score >= 70:
			return 'B'
		elif self.__score >= 60:
			return 'C'
		else:
			return 'D'
	
	def get_score(self):
		print('%s: %s'%(self.__name,self.__score))
	
	def set_gender(self, gender):
		self.__gender = gender
	
	def get_gender(self):
		return self.__gender
		
#jackie = Student('Jackie',78)
#jackie.get_score()
#print(jackie._Student__name)
#jackie.__name
bob = Student('Bob', 'male')
if bob.get_gender() != 'male':
	print('测试失败！')
else:
	bob.set_gender('female')
	if bob.get_gender() != 'female':
		print('测试失败！')
	else:
		print('测试成功！')