from array import *

forest = list()

with open("map.txt") as f:
    forest = f.read().splitlines()

forest_len = len(forest)    

def count_trees(slope_x, slope_y):
    tree_count = 0
    toboggan_index = 0

    for pos in range(0, forest_len, slope_y):
        line_size = len(forest[pos])

        if toboggan_index >= line_size:
            toboggan_index = toboggan_index % line_size

        if forest[pos][toboggan_index] == '#':
            tree_count += 1
        toboggan_index += slope_x

    return tree_count

prod = 1 
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

for s in slopes:
    prod = prod * count_trees(s[0], s[1])

print(prod)