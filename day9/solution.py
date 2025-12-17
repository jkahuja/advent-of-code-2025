import sys

positions = []

for line in sys.stdin:
    positions.append(tuple(int(num) for num in line.split(","))) 

max_area = 0

for i in range(0, len(positions)):
    for j in range(i + 1, len(positions)):
        max_area = max((abs(positions[i][0] - positions[j][0]) + 1) * (abs(positions[i][1] - positions[j][1]) + 1), max_area)
         
print(max_area)
