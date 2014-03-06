# -*- coding:utf-8 -*-
# 导入函数
from sys import argv

script, input_file = argv
# 定义三个函数print_all,rewind,print_a_line
def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print line_count, f.readline()
# 打开文件
current_file = open(input_file)

print "First let's print the whole file:\n"
# 将参数传递个函数
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# 将参数传递个函数
rewind(current_file)

print "Let's print three lines:"
# 定义变量并赋值
current_line = 1
# 向函数传递两个参数
print_a_line(current_line, current_file)
# 定义变量
current_line = current_line + 1
# 向函数传递两个参数
print_a_line(current_line, current_file)
# 定义变量
current_line = current_line + 1
# 向函数传递两个参数
print_a_line(current_line, current_file)
