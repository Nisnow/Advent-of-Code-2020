
f = open("data.txt", "r")

vals = {}

for val in f:
    vals.update({int(val): 2020-int(val)})

keys = vals.keys()

for y in vals:
    currentTarget = 2020 - y
    nums = set()

    for z in vals:
        if (currentTarget - z) in nums:
            print(y * z * (currentTarget - z))
        else:
            nums.add(z)
        