tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# 将转义序列和格式化字符串组合到一起，创建一种更复杂的格式。
print "\'hello world'\n\tchina\n\v%s" % tabby_cat

'''
记得 %r 格式化字符串吗？使用 %r 搭配单引号和双引号转义字符打印一些字符串出来。将 %r
和 %s 比较一下。注意到了吗？%r 打印出来的是你作为程序员写在脚本里的东西，而 %s 打印
的是你作为用户应该看到的东西。
'''
print "\'%r\'" % persian_cat
print "\'%s\'" % persian_cat