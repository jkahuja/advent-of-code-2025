import sys

grid = []

for line in sys.stdin:
    grid.append(line.strip())

# find start position
for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        if grid[i][j] == 'S':
            start_pos = (i, j)
            break

positions = [start_pos]
cur_row = start_pos[0]
num_splits = 0

while cur_row < len(grid) - 1:
    new_positions = set()
    cur_row += 1
    for cur_pos in positions:
        cur_col = cur_pos[1]
        if grid[cur_row][cur_col] == '^':
            num_splits += 1
            new_positions.add((cur_row, cur_col - 1))
            new_positions.add((cur_row, cur_col + 1))
        else:
            new_positions.add((cur_row, cur_col))
    positions = list(new_positions)

print(num_splits)
