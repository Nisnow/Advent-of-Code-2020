
# Given a puzzle input with each line formatted as 
#
#   x-y @: abccdef
#
# With x as the index of where @ could appear and y as the index
# of where @ could appear in the string where only @ can appear in either
# index x or y BUT NOT BOTH, this finds the number of valid passwords
# in the puzzle input given this format.

f = open("data.txt", "r")

data = []

validCount = 0

for line in f:

    # Split line as array [min, max, char, password]
    sep = line.split(" ")
    rangeVal = sep[0].split('-')

    # Extract min and max from format 'x-y' 
    minInd = int(rangeVal[0])
    maxInd = int(rangeVal[1])

    # Remove the colon in the character string
    char = sep[1][0]
    pswrd = sep[2]

    firstExists = pswrd[minInd-1] == char
    secExists = pswrd[maxInd-1] == char

    # XOR operation to find valid passwords
    if firstExists != secExists:
        validCount += 1

print(validCount)