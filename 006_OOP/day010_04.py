#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# 面向对象高级编程-枚举类

from enum import Enum,unique

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)
#value属性则是自动赋给成员的int常量，默认从1开始计数。	

#既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Web = 3
	Thu = 4
	Fri = 5
	Sat = 6
day1 = Weekday.Mon
print(day1)
print(Weekday['Mon'])
print(Weekday(1))
print(Weekday.Mon)
print(Weekday.Mon.value)
print(day1 == Weekday.Mon)

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
		
# 测试:
bart = Student('Bart', Gender(0))
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')