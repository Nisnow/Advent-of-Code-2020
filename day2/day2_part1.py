
# Given a puzzle input with each line formatted as 
#
#   x-y @: abcdef
#
# With x as the minimum count required of a character '@' in 
# a password and y the maximum number of occurances the character
# can appear in the password, this finds the number of valid 
# passwords in the given puzzle input given this format.

f = open("data.txt", "r")

data = []

validCount = 0

for line in f:

    # Split line as array [min, max, char, password]
    sep = line.split(" ")

    # Extract min and max from format 'x-y' 
    rangeVal = sep[0].split('-')

    minCount = int(rangeVal[0])
    maxCount = int(rangeVal[1])

    # Remove the colon in the character string
    char = sep[1][0]
    pswrd = sep[2]

    count = pswrd.count(char)

    # Valid password
    if count >= minCount and count <= maxCount:
        validCount += 1

print(validCount)