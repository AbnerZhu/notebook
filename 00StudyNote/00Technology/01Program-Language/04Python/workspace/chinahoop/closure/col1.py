#!/usr/bin/env python
# coding:utf-8

def line_conf():
	def line(x):
		return 2*x + 1
	return line # 返回函数对象

my_line = line_conf()
print(my_line(5))