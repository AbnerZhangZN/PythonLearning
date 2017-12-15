#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#setup 15 高级特性-生成器

print([x*x for x in range(10)])
g = (x * x for x in range(10))
for s in g:
	print(s)

def fib(max):
	n, a, b = 0, 0, 1
	while n<max:
		print(b)
		a, b = b, a+b
		n = n+1
	return 'done'
fib(10)

def fibG(max):
	n, a, b = 0, 0, 1
	while n<max:
		yield b
		a, b, n = b, a+b, n+1
	return 'done'
for s in fibG(10):
	print(s)
g = fibG(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Genarator return value:', e.value)
		break

def triangles():
	L = []
	while True:
		oldL = L[:]
		L.append(1)
		i = 0
		if len(L)>1:
			while i<len(L)-1:
				if i==0:
					L[i] = 1
					i = i+1
					continue
				L[i] = oldL[i-1]+oldL[i] 
				i = i+1
			L[-1] = 1
		#print(L)
		yield L
	return 'Done'
	
def trianglesSimple():
	L = [1]
	while True:
		yield L
		L = [1] + [L[i]+L[i+1] for i in range(len(L)-1)] + [1]
n = 0
results = []
for t in trianglesSimple():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
	
	
	
	
	
	
	
	
	
	
	