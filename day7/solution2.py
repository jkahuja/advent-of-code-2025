import sys
from collections import defaultdict

grid = []

for line in sys.stdin:
    grid.append(line.strip())

# find start position
for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        if grid[i][j] == 'S':
            start_pos = (i, j)
            break

positions = [(start_pos[0], start_pos[1], 1)]
cur_row = start_pos[0]
num_splits = 1

while cur_row < len(grid) - 1:
    new_positions = defaultdict(int)
    cur_row += 1
    for _, cur_col, cur_splits in positions:
        if grid[cur_row][cur_col] == '^':
            num_splits += cur_splits
            new_positions[(cur_row, cur_col - 1)] += cur_splits
            new_positions[(cur_row, cur_col + 1)] += cur_splits
        else:
            new_positions[(cur_row, cur_col)] += cur_splits
    positions = [(key[0], key[1], value) for key, value in new_positions.items()]

print(num_splits)

