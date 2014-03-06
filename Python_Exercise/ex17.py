# -*- coding:utf-8 -*-
# 导入两个方法
from sys import argv
from os.path import exists
# 定义两个变量
script, from_file, to_file = argv
# 打印from_file,to_file变量
print "Coping from %s to %s" % (from_file, to_file)
# we could do these two on one line too, how?
# 用变量in_file存储文件内容
in_file = open(from_file)
# 读取文件
indata = in_file.read()
# 打印数据长度
print "The input file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
# 键盘输入
raw_input()
# 用写的方式打开文件
out_file = open(to_file, 'w')
# 向文件写入内容
out_file.write(indata)
print "Alright, all done."
# 关闭文件
out_file.close()
in_file.close()