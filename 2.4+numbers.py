# numbers can be of 3 types
# dynamically typed language, on run time the type is checked by the compiler
integer_num = 23
float_num = 23.233333
complex_num = 23j
# we dont use complex numbers a lot in this course so we will end the discussion on them here
# OPERATIONS
# addition
x = 23
y = 2
addition = x + y
print(addition)
# subtraction
subtraction = x - y  # 21
print(subtraction)
# multiplication
multiplication = x * y  # 46
print(multiplication)
# division
# there are two types of divisions inn python, one is called floor division and the other is simple division
# simple division
div_simple = x / y  # 11.5
print(div_simple)
# floor division is simply the same division without the decimal part {the part after the point}
div_floor = x // y  # 11
print(div_floor)
# modulus operator
mod = x % y  # 1 returns the remainder after dividing x by y
print(mod)