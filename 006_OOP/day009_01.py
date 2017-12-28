#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# 面向对象高级编程-使用__slots__限制类属性

# 由于python是动态语言，在定义了一个class，创建了一个class的实例后，可以给该实例绑定任何属性和方法
class Student(object):
	pass
	
s = Student()
s.name = 'Jackie'
s.age = '21'
print(s.name, s.age)

def set_score(self, score):
	self.score = score

from types import MethodType
s.set_score = MethodType(set_score, s)
s.set_score(89)
print(s.score)

def set_age(self, age):
	self.age = age
Student.set_age = set_age
s2 = Student()
s2.set_age(17)
s.set_age(23)
print(s.age, s2.age)

#给实例添加设置方法和属性只对当前属性和方法有效，可以直接对该类绑定方法和属性

#使用__slots__可以限制类和实例的属性,但是不限制子类，子类的限制是自身的__slots__和父类的__slots__
class StudentTmp(object):
	__slots__ = ('name','age')

sTemp = StudentTmp()
#sTemp.score = 20
sTemp.age = 20


