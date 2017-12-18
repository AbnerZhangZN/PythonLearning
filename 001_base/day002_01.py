#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#setup 5 练习-使用list和tuple
#列表：list 有序列表，可变 []
roommates=['I','Me','W0']
print(len(roommates))
print(roommates[0])
print(roommates[-1])
roommates.append('我')
print(roommates)
roommates.insert(1,'whzhang1')
print(roommates)
roommates.pop()
print(roommates)

languages=[['Java','Kotlin'],'Python','JavaScript',123]
print(len(languages))
#元组：tuple 有序列表，不可变更安全[]
tools=(1,)
toools=(1,2,3)
print(tools)
print(len(tools))
print(len(toools))

#练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[1])
print(L[0][0])
print(L[1][1])
print(L[2][2])

L = (
    ('Apple', 'Google', 'Microsoft'),
    ('Java', 'Python', 'Ruby', 'PHP'),
    ('Adam', 'Bart', 'Lisa')
)

print(L[1])
print(L[0][0])
print(L[1][1])
print(L[2][2])