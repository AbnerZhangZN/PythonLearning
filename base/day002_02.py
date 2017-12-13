#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#setup 6 练习-条件判断
age = 2
if age>18:
	print('Your age is',age)
	print('Adult!')
elif age>6:
	print('Teenager!')
else:
	print('Kid!')

age=int(input('Please input your age:'))
if age>18:
	print('Adult!')
else:
	print('Child!')
	
'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
height=1.75
weight=80.5
BMI=weight/height/height
print(BMI)
if BMI<18.5:
	print('低于18.5：过轻')
elif BMI<25:
	print('18.5-25：正常')
elif BMI<28:
	print('25-28：过重')
elif BMI<32:
	print('28-32：肥胖')
else:
	print('死胖子')