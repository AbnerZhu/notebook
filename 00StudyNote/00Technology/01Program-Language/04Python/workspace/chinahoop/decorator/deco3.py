#!/usr/bin/env python
# coding:utf-8

# 新的包装层
def pre_str():
	# 旧的装饰器
	def decorator(F):
		def new_F(a, b):
			print("input: ", a, b)
			return F(a, b)
		return new_F
	return decorator


# 计算平方和
@pre_str('hi + ')
def square_sum(a, b):
	return a ** 2 + b ** 2


# 计算平方差
@pre_str('hi - ')
def square_diff(a, b):
	return a ** 2 - b ** 2

print(square_sum(3, 4))
print(square_diff(3, 4))