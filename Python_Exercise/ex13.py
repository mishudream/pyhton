from sys import argv

first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

'''
# 加分练习
# 1. 再写两个脚本，其中一个接受更少的参数，另一个接受更多的参数，在参数解包时给它们取一些有意义的变量名
from sys import argv
script, name = argv
print "The script is called:", script
print "My name is:", name

# 将 raw_input 和 argv 一起使用，让你的脚本从用户手上得到更多的输入。
from sys import argv
script, user_name = argv
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
'''