# -*- coding:utf-8 -*-

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# 加分题
# 错误信息：没有定义car_pool_capacity,程序执行时无法找到。
# File "ex4.py", line 8, in <module>
# average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# 更多的加分习题:
# 1. 我在程序里用了 4.0 作为 space_in_a_car 的值，这样做有必要吗？如果只用 4 会有什么问题?
# 答：
#2. 记住 4.0 是一个“浮点数”，自己研究一下这是什么意思。
#3. 在每一个变量赋值的上一行加上一行注解。
#4. 记住 = 的名字是等于(equal)，它的作用是为东西取名。
#5. 记住 _ 是下划线字符(underscore)。
#6. 将 python 作为计算器运行起来，就跟以前一样，不过这一次在计算过程中使用变量名来做计算，常见的变量名有 i, x, j 等等。