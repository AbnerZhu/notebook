#! /usr/bin/env python
#coding:utf-8

class Me(object):
	def test(self):
		print "Hello"

def new_test():
	print "New Hello"

me = Me()

print hasattr(me. "test")			# 检查 me 对象是否有 test 属性
print getattr(me, "test") 			# 返回 test 属性
print setattr(me, "test", new_test) # 将 test 属性设置为 new_test
print delattr(me,  "test") 			# 删除 test 属性
print isinstance(me, Me)			# me 对象是否为 Me 类生成的对象（一个 instance）
print issubclass(Me, object) 		# Me 类是否为 object 类的子类
