# -*- coding:utf-8 -*-
# 定义四个函数，分别进行加、减、乘、除运算
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDEING %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"
# 向函数传递参数，并将结果赋值给age
age = add(30, 5)
# 向函数传递参数，并将结果赋值给height
height = subtract(78, 4)
# 向函数传递参数，并将结果赋值给multiply
weight = multiply(90, 2)
# 向函数传递参数，并将结果赋值给divide
iq = divide(100, 2)
# 打印结果
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
# 进行加减乘除运算
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what, "Can you do it by hand?"