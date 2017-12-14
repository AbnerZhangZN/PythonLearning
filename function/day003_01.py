#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#setup 10 函数-函数的参数 重点难点
def power(x,n=2): #n=2 是默认参数，可以在调用参数的只传第一个
	s=1
	while n>0:
		n = n - 1
		s = s * x
	return s

print(power(5))
print(power(5,3))
print(power(5,4))

def mind(*num): #可变参数，传入list或者tuple
	sum = 0
	for n in num:
		sum = sum + n
	return sum
	
print(mind(0,1,2,3))

extra={'city':'Beijing','Job':'JavaDeveloper'}
def person(name, age, **kw):#关键字参数 相当于传入dict
	print('Name:',name,'Age:',age,'Other:',kw)

person('Xiaoming',23 , **extra)

#命名关键字参数 和关键字参数**kw不同，
#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person1(name, age, *, city, job): 
	print(name, age, city, job)
person1('Xiaoming1', 23, city='Beijing', job='JavaDeveloper')

def person2(name, age, *, city='Suzhou', job): 
	print(name, age, city, job)
person2('Xiaoming2', 23, job='JavaDeveloper')

def person3(name, age, *args, city, job):
	print(name, age, args, city, job)
person3('Xiaoming3', 23, 'a', 2, city='Shanghai', job='JavaDeveloper')

#参数组合  必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
def person4(name, age=18, **kw, address)
	print('name=', name, 'age=',age, 'kw=',kw, 'address=', address)
#('Xiaoming4',20, **extra, address='科灵路')


