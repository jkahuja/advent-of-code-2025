import copy
import sys

grid = []

for line in sys.stdin:
    grid.append(list(line.strip()))

total = 0


def can_access(row_idx, col_idx):
    num_rolls = 0
    for i in range(row_idx - 1, row_idx + 2):
        for j in range(col_idx - 1, col_idx + 2):
            if (
                (i == row_idx and j == col_idx)
                or i < 0
                or i >= len(grid)
                or j < 0
                or j >= len(grid[0])
            ):
                continue
            if grid[i][j] == '@':
                num_rolls += 1
    return num_rolls < 4


done = False

while not done:
    done = True
    new_grid = copy.deepcopy(grid)
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "@":
                if can_access(i, j):
                    done = False
                    total += 1
                    new_grid[i][j] = '.'
    grid = new_grid

print(total)

