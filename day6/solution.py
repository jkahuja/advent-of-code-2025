import sys
import re

grid = []
total = 0

for line in sys.stdin:
    line = re.sub(' +', ' ', line.strip())
    grid.append(line.split(' '))

for j in range(len(grid[0])):
    operands = []
    for i in range(len(grid) - 1):
        operands.append(grid[i][j])
    operation = grid[len(grid) - 1][j]
    expression = operation.join(operands)
    total += eval(expression)
        
                
            
print(total)
