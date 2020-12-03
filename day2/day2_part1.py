
f = open("data.txt", "r")

data = []

validCount = 0

for line in f:
    # Split line as array [min, max, char, password
    sep = line.split(" ")
    rangeVal = sep[0].split('-')

    minCount = int(rangeVal[0])
    maxCount = int(rangeVal[1])

    char = sep[1][0]
    pswrd = sep[2]

    count = pswrd.count(char)
    if count >= minCount and count <= maxCount:
        validCount += 1

print(validCount)