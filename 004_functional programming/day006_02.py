#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#setup 19 函数式编程-匿名函数

#关键字lambda表示匿名函数，冒号前面的x表示函数参数
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
L1 = list(filter(lambda x:x%2==1, range(1,20)))
print(L1)