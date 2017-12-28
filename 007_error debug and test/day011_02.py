#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# 错误、调试和测试-错误处理

import logging
def func():
	try:
		print('try...')
		r  = 10/0
		print('result:', r)
	except ZeroDivisionError as e :
		print('except ： ', e)
		logging.exception(e)
		#抛出错误
		raise ValueError('invalid value: 0')
	finally:
		print('finally ...')
	print('END')
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，
#则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行
#完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
# python 所有的错误都是从BaseException类派生的
#Python内置的logging模块可以非常容易地记录错误信息