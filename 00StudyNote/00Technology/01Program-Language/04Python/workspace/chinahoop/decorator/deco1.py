#!/usr/bin/env python
# coding:utf-8

# 计算平方和
def square_sum(a, b):
	print("input: ", a, b)
	return a ** 2 + b ** 2


# 计算平方差
def square_diff(a, b):
	print("input: ", a, b)
	return a ** 2 - b ** 2

print(square_sum(3, 4))
print(square_diff(3, 4))