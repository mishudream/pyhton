﻿from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

"""
加分题
1.写一个和上一个练习类似的脚本，使用 read 和 argv 读取你刚才新建的文件。

from sys import argv
script, filename = argv
txt = open(filename)
print txt.read()

2.文件中重复的地方太多了。试着用一个 target.write() 将 line1, line2, line3 打
印出来，你可以使用字符串、格式化字符、以及转义字符

target.write("%s\n%s\n%s\n" % (line1, line2, line3))
"""