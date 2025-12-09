import sys


num_zeros = 0
cur_pos = 50

for line in sys.stdin:
    direction = line[0]
    turns = int(line[1:])
    if direction == 'L':
        cur_pos = (cur_pos - turns) % 100
    else:
        cur_pos = (cur_pos + turns) % 100
    if cur_pos == 0:
        num_zeros += 1

print(num_zeros)
