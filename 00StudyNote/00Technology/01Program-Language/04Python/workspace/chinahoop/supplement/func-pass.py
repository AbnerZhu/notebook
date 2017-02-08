#! /usr/bin/env python
#coding:utf-8

a = 1

def change_integer(a):
	a = a + 1
	pass # **pass 关键字表示占位， 不执行具体操作
	return a

print change_integer(a)
print a

########
b = [1, 2, 3]
def change_list(b):
	b[0] = b[0] + 1
	return b

print change_list(b)
print b
