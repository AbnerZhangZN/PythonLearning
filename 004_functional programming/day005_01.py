#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#setup 17 函数式编程-高阶函数

# 变量可以指向函数,函数名也是变量
f = abs
print(f(-200))

# 高阶函数：一个函数就可以接收另一个函数作为参数
def abs_add(x, y, fun):
	return fun(x) + fun(y)

print(abs_add(-20, 200, abs))

#map()  map()函数接收两个参数，一个是函数，一个是Iterable，
#			map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def funMultiply(x):
	return x * x
r = map(funMultiply, list(range(1, 11)))
print(list(r))
print(list(map(str,list(range(1,11)))))

#reduce() reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
#			这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def normalize(name):
	L = [m.lower() for m in name]
	L[0]=L[0].upper()
	return reduce(lambda a,b: a+b, L)
L1 = ['adam','LISA','barT']
print(list(map(normalize, L1)))	

#求积
def prod(L):
	return reduce(lambda a,b: a*b, L)
print(prod([x for x in range(1,6)]))

DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def char2num(s):
	return DIGITS[s]
def str2float(s):
	left = s.split('.')[0]
	right = s.split('.')[1]
	return reduce(lambda x,y: x*10+y,map(char2num,left))+reduce(lambda x,y:x+0.1*y,map(char2num,right))*0.1

print(str2float('152.12')+str2float('23.23'))
print('12021.234'.split('.'))
print(6%10)
#----------------filter
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
#		filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#素数生成器 埃氏筛法
# 1 生成从3 开始的奇数序列
def _odd_iter():
	n = 1
	while True:
		n = n+2
		yield n
# 2 筛选函数
def _not_divisible(n):
	return lambda x:x%n>0
# 3 素数生成器，不断返回
def primes():
	yield 2
	odd_iter = _odd_iter()
	while True:
		n = next(odd_iter)
		yield n
		odd_iter = filter(_not_divisible(n),odd_iter)
#test
#for n in primes():
#	if n < 1000:
#		print(n)
#	else:
		break

def _nature_num():
	n = 0
	while True:
		yield n
		n = n + 1

# 1 转换为字符串列表
# 2 判断L[n]===L[-n-1] n<len(L)/2
print(51//2)
def _is_numback(n):
	L = str(n)
	for b in range((len(L)+1)//2):
		if L[b]!=L[-b-1]:
			return False
	return True
def _is_numback2(n):
	return str(n)==str(n)[::-1]
print('1-1000', list(filter(_is_numback, range(1,1000))))
print('1-1000', list(filter(_is_numback2, range(1,1000))))

#------------------------sorted()
print(sorted([23,3,-5,33,-66]))
print(sorted([23,3,-5,33,-66], key=abs))
print(sorted(['Abner','Bob','jackie','Zack'], key=str.lower, reverse=True))
L = [('Bob',75),('Jack',88),('Mark',90),('Abner',79)]
def by_name(t):
	return t[0].lower()

print(sorted(L,key=by_name))

def by_score(t):
	return t[1]
print(sorted(L, key=by_score, reverse=True))