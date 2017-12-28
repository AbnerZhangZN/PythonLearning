#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# 错误、调试和测试-调试

#方法一、简单粗暴，直接用print()把可能有问题的变量打印出来
#方法二、断言 assert: 表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
#方法三、logging logging.basicConfig(level=logging.INFO) 有debug，info，warning，error四个级别
#			level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了
#方法四、pdb 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码，命令n可以单步执行代码
			
import logging,pdb
def fun(s):
	n = int(s)
	#print()
	print('print---n= %d' %n)
	#断言  python -0 *.py 可以关闭assert
	assert n != 0, 'n is zero!'
	#logging
	logging.info('logging---n= %d' %n)
	#pdb 
	pdb.set_trace() #运行到这里停止--断点
	return 10/n
	
print(fun('1'))