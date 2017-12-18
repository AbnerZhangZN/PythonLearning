#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#setup 9 函数-自定义函数
def my_abs(x):
	if x>0:
		return x
	else:
		return -x

print(my_abs(-12))

def nop():
	pass

nop()

import math

def move(x,y,step,angle=0):
	nx = x + step*math.cos(angle)
	ny = y + step*math.sin(angle)
	return nx,ny

print(move(3,4,3,30))#ython的函数返回多值其实就是返回一个tuple

