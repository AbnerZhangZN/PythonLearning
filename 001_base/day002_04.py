#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#setup 7 练习-使用dict(字典)和set
#dict 类似于map
d={'Jack':90,'Michael':60,'whzhang1':59}
print(d['Jack'])
d['whzhang1']=100
print(d['whzhang1'])
print('Jack' in d)
print(d.get('Jack'))
d.pop('Michael')
print(d)
#set
s=set([1,2,2,3,4])
print(s)
s.add(5)
print(s)
sNew=set([2,3,5,6])
print(s & sNew)
print(s | sNew)


d = {(1,2,3):'(1,2,3)'}#,(1,([2,3],)):'(1,[2,3])'}
s = set((1,[2,3]),(1,2,3))
print(d)
#print(d[(1,2,3)])
#print(d.get((1,[2,3])))
#print(s)
#print(s.get((1,2,3))