#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#setup 6 练习-循环

aList = list(range(5))
print(aList)

sum = 0;
xList = list(range(101))
print(xList)
yList = range(101)
for x in yList:
	sum = sum + x
print(sum)

sum = 0
n=99
while n>0:
	sum = sum + n
	n = n - 2
print(sum)

n=0
while n<100:
	n = n + 1
	if n>10:
		break
	if n % 2==0:
		continue
	print(n)
	
#死循环
print('死循环')
n=3
while n<100:
	n = n + 1
	if n>98:
		n = n - 98
	print(n)
