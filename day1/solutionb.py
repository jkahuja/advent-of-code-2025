import sys


num_zeros = 0
cur_pos = 50

for line in sys.stdin:
    direction = line[0]
    turns = int(line[1:])
    for i in range(0, turns):
        if direction == "L":
            cur_pos -= 1
            if cur_pos == -1:
                cur_pos = 99
            if cur_pos == 0:
                num_zeros += 1
        else:
            cur_pos += 1
            if cur_pos == 100:
                cur_pos = 0
            if cur_pos == 0:
                num_zeros += 1


print(num_zeros)
