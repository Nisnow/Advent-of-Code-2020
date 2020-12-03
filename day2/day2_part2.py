
f = open("data.txt", "r")

data = []

validCount = 0

for line in f:
    # Split line as array [min, max, char, password]
    sep = line.split(" ")
    rangeVal = sep[0].split('-')

    minInd = int(rangeVal[0])
    maxInd = int(rangeVal[1])

    char = sep[1][0]
    pswrd = sep[2]

    firstExists = pswrd[minInd-1] == char
    secExists = pswrd[maxInd-1] == char

    if firstExists != secExists:
        validCount += 1

print(validCount)