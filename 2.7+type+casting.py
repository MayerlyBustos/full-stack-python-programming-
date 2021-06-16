# in programming we deal with many situations, one of them is type casting
# consider the following example
age = 22
# print("Her age is : " + age)  # throws an error (not string)

# python doesnt know how to add a number into a string
# so we have convert it
# converting a number to string
age_in_string = str(age)
print("Her age is : " + age_in_string)  # works
# we can also convert a string into a number if it is valid
phone = "1234-123"
# phone_int = int(phone)  # error because of the -
phone = "1234123"
phone_int = int(phone)  # works
print(phone_int+2)
# converting to float
temperature = "361.23"
temperature_in_float = float(temperature)
print(temperature_in_float+2.11)  # 363.34
# so whenever you are doing something where types are mixed up make sure to do type casting
