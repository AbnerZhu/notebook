#! /usr/bin/env python
def gen():
	a = 10
	yield a
	a = a * 10
	yield a
	yield 1000

for i in gen():
	print i