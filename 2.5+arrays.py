# as we discussed that arrays store similar kind of data
# though in python we can store different types of data in an array but still
# its important to keep similar data as a good practice, we can also do type casting which we will study soon
temperatures = [234, 235, 52, 23, 4, 1, 25, 23, 5, 2]
print(temperatures)
# length
number_of_temperatures = len(temperatures)  # 10
print(number_of_temperatures)
# accessing a specific value in the array
# index based numbering/counting
print(temperatures[0])
# changing a value
temperatures[0] = 12
print(temperatures)  # first value is changed
# example 2
# weight of first 5 players in your football team
weights = [67, 78, 64, 89, 77]
print(weights[3])  # fourth player's weight
# this is it for arrays for now
comida_favorita = [["Mandarina", "citrico"],["Sandia", "dulce"]]
cf = comida_favorita[1][0]
print(cf)
