
forest = list()

with open("map.txt") as f:

    # splitlines() will remove all newlines in the input
    forest = f.read().splitlines()
    
tree_count = 0
toboggan_index = 0

for pos in forest:
    line_size = len(pos) 

    # Wraps around back to the left of the slope since the patterns are repeating
    if toboggan_index >= line_size:
        toboggan_index = toboggan_index % line_size

    # Encountered a tree; count it
    if pos[toboggan_index] == '#':
        tree_count += 1
    toboggan_index += 3

print(tree_count)