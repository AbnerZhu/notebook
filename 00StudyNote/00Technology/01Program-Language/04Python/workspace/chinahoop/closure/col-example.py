#!/usr/bin/env python
# coding:utf-8

def line_conf(a, b):
	def line(x):
		return a*x + b
	return line # 返回函数对象

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))