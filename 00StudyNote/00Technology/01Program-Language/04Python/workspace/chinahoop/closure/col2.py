#!/usr/bin/env python
# coding:utf-8

def line_conf():
	b = 15
	def line(x):
		return 2*x + b
	return line # 返回函数对象

b = 5
my_line = line_conf()
print(my_line(5))