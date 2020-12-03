
# Finds two numbers in the puzzle input that add up to 2020

f = open("data.txt", "r")

vals = {}

# In a map, subtract all values from 2020 to find the first number
for val in f:
    vals.update({int(val): 2020-int(val)})

keys = vals.keys()

# Find a number in the map whose key and value in the map add up to 2020
# and that both exist in the puzzle input
for y in vals:
    if (y + vals[y] == 2020 and vals[y] in keys):
        print(y* vals[y],)