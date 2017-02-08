#!/usr/bin/env python
# coding:utf-8

def deco(F):
	def new_F(a, b):
		print("input: ", a, b)
		return F(a, b)
	return new_F

# 计算平方和
@deco
def square_sum(a, b):
	return a ** 2 + b ** 2


# 计算平方差
@deco
def square_diff(a, b):
	return a ** 2 - b ** 2

print(square_sum(3, 4))
print(square_diff(3, 4))