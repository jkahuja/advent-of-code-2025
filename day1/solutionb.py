import sys


num_zeros = 0
cur_pos = 50

for line in sys.stdin:
    direction = line[0]
    turns = int(line[1:])
    if direction == 'L':
        new_pos = (cur_pos - turns) % 100
    else:
        new_pos = (cur_pos + turns) % 100
    through_zero_left = new_pos > cur_pos and direction == 'L'
    through_zero_right = cur_pos > new_pos and direction == 'R'
    many_turns = turns >= 99
    if new_pos == 0 or ((through_zero_left or through_zero_right) and cur_pos != 0) or many_turns:
        num_zeros += 1
    cur_pos = new_pos

print(num_zeros)
