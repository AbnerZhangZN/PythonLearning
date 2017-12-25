#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# 面向对象编程-实例属性和类属性

#实例属性属于各个实例所有，互不干扰；
#类属性属于类所有，所有实例共享一个属性；
#不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误

class Student(object):
	name = 'Student'
s = Student()
print(s.name)
print(Student.name)
s.name='Jack'
print(s.name)
print(Student.name)
del s.name
print(s.name)

class Student1(object):
	count = 0
	
	def __init__(self, name):
		Student1.count += 1
		self.name = name

if Student1.count != 0:
    print('测试1失败!')
else:
    bart = Student1('Bart')
    if Student1.count != 1:
        print('测试失败!')
    else:
        lisa = Student1('Bart')
        if Student1.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student1.count)
            print('测试通过!')