from array import *

forest = list()

with open("map.txt") as f:
    forest = f.read().splitlines()
    
tree_count = 0
toboggan_index = 0

# First line doesn't matter
for pos in forest:
    line_size = len(pos) 

    if toboggan_index >= line_size:
        toboggan_index = toboggan_index % line_size

    if pos[toboggan_index] == '#':
        tree_count += 1
    toboggan_index += 3

print(tree_count)