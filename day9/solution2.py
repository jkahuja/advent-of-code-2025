import sys

positions = []

for line in sys.stdin:
    positions.append(tuple(int(num) for num in line.split(","))) 

green_rows = []
green_cols = []

for i in range(0, len(positions)):
    for j in range(i + 1, len(positions)):
        pos1 = positions[i]
        pos2 = positions[j]
        if pos1[0] == pos2[0]:
            green_cols.append((pos1[0], min(pos1[1], pos2[1]), max(pos1[1], pos2[1])))
        else:
            green_rows.append((pos1[1], min(pos1[0], pos2[0]), max(pos1[0], pos2[0])))

green_cols.sort()
green_rows.sort()

max_area = 0

for i in range(0, len(positions)):
    for j in range(i + 1, len(positions)):
        pos1 = positions[i]
        pos2 = positions[j]
        is_valid = True

        top_row = min(pos1[1], pos2[1]) 
        bottom_row = max(pos1[1], pos2[1])
        


        left_col = min(pos1[0], pos2[0])
        right_col = max(pos1[0], pos2[0])

        if is_valid:
            max_area = max((abs(positions[i][0] - positions[j][0]) + 1) * (abs(positions[i][1] - positions[j][1]) + 1), max_area)
         
print(max_area)
