
f = open("data.txt", "r")

vals = {}

for val in f:
    vals.update({int(val): 2020-int(val)})

keys = vals.keys()

for y in vals:
    if (y + vals[y] == 2020 and vals[y] in keys):
        print(y* vals[y],)