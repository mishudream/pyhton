# -*- coding:utf-8 -*-

my_name = 'Zed A. Shaw'
my_age = 35 # not a line
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# 加分题
# 第一题：去掉"my_"
name = 'Zed A. Shaw'
age = 35 # not a line
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# 第二题：更多的格式化字符
school = "Bei Jing University"
print "I come from %r." % school
print("%+10x" % 10)
print("%04d" % 5)
print("%6.3f" % 2.3)
print("%e" % 2.3)

# 单位转换
# 1、英寸转换为厘米
inch = 1
conversion = 30.5
print "One inch equals %.2f cm." % (inch * conversion)

# 2、磅转换为千克
sterling = 1
conversion = 0.454
print "One sterling equals %.3f kg." % (sterling * conversion)

