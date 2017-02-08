#!/usr/bin/env python

class Bird(object):
	feather = True

class Chicken(Bird):
	fly = False
	def __init__(self, age):
		self.age = age

chick = Chicken(2)

print(Bird.__dict__)
print(Chicken.__dict__)
print(chick.__dict__)

# print('-------------------')

# chick.__dict__['age'] = 3
# print(chick.__dict__['age'])

# chick.age = 10
# print(chick.age)