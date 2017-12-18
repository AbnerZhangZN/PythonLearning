#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#setup 14 高级特性-列表生成式
#单层循环
print([x * x for x in range(1, 11)])
#单层循环后加判断
print([x * x for x in range(1, 11) if x % 2 == 0])
#两层循环 全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')])# os.listdir可以列出文件和目录

d = {'a':'1','b':'2','c':'3'}
print([k + '=' + v for  k,v in d.items()])

L = ['Hello','World','Java','IBM','Apple','Python']
print([s.lower() for s in L])
print([s.upper() for s in L])

L0 = ['Hello','World',22,None,'Java','IBM','Apple','Python','231asfADS']
print([s.lower() for s in L0 if isinstance(s, str)])