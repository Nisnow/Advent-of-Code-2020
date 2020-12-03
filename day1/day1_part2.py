
# Finds three numbers in the puzzle input that add up to 2020

f = open("data.txt", "r")

vals = {}

# In a map, subtract all values from 2020 to find the first number
for val in f:
    vals.update({int(val): 2020-int(val)})

keys = vals.keys()

for y in vals:

    # The sum of the second two numbers
    currentTarget = 2020 - y
    nums = set()

    for z in vals:

        # Find the third value
        if (currentTarget - z) in nums:
            print(y * z * (currentTarget - z))
        else:
            # Keep track of this number later in case it's one of the numbers
            # that adds up to 2020
            nums.add(z)
        