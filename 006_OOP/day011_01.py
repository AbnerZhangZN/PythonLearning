#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# 面向对象高级编程-元类

class Hello(object):
	def hello(self, name='world'):
		print('Hello, %s' % name)
h = Hello()
print(type(Hello))
print(type(h))
#type()函数是一个类型(class)或变量的类型，类Hello的类型是type,h实例的类型是class Hello

def fn(self, name='world'):
	print('Hello,type %s ' %name)
	
HelloType = type('HelloType',(object,),dict(hello=fn))

ht = HelloType()
ht.hello()
#要创建一个class对象，type()函数依次传入3个参数：
#1、class的名称；
#2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

#python 作为动态语言，可以在运行期动态创建类，很简单；但静态语言Java（java本身是静态语言，后来加入很多动态特性！）
#如果需要在运行期创建类，必须构造源代码字符串再调用编译器生成字节码实现，可以算作动态编译，非常复杂


#metaclass
#创建一个对象：先定义metaclass->创建类->创建实例(对象)

#通过ListMetaclass.__new__()来创建
#类似Java重写父类的方法,这里重写了type的__new__函数，然后又调用了一次
#__new__()方法接收到的参数依次是：
#	1、当前准备创建的类的对象；
#	2、类的名字；
#	3、类继承的父类集合；
#	4、类的方法集合。
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
	pass
	
myList = MyList([])
myList.add(1)
print(myList)