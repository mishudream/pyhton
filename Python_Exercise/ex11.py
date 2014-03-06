print "How old are you?",
age = int(raw_input()) # 加分第二题
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

'''
# 1. 上网查一下 Python 的 raw_input 实现的是什么功能。
# 答：raw_input 读取输入值，返回的是字符串类型

# 2. 你能找到它的别的用法吗？测试一下你上网搜索到的例子。

# 3. 用类似的格式再写一段，把问题改成你自己的问题。
print "Why learn?"
answer = raw_input()
print "Continued efforts! %s" % answer
'''