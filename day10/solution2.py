import sys
import re
import copy
from itertools import combinations_with_replacement

def bfs(goal_state, buttons):
    print(goal_state)
    cur_state = [0] * len(goal_state)
    queue = []
    queue.append((tuple(cur_state), 0))
    min_presses = None
    while queue:
        min_val = None
        min_idx = None
        zero_inds = set()
        cur_state, num_presses = queue.pop(0) 
        for i in range(0, len(goal_state)):
            if goal_state[i] == cur_state[i]:
                zero_inds.add(i)
                continue
            if not min_val:
                min_val = (goal_state[i] - cur_state[i])
                min_idx = i
            elif (goal_state[i] - cur_state[i]) < min_val:
                min_val = (goal_state[i] - cur_state[i])
                min_idx = i
        if not min_val:
            return min_presses
        possible_buttons = []
        for button in buttons:
            if min_idx in button and not any(ind in zero_inds for ind in button):
                possible_buttons.append(button)
        for button_set in combinations_with_replacement(possible_buttons, min_val):
            is_valid = True
            button_valid = True
            new_state = list(cur_state)
            for button in button_set:
                for pos in button:
                    new_state[pos] += 1
            for i in range(len(new_state)):
                if new_state[i] > goal_state[i]:
                    is_valid = False
                    break
            if new_state == goal_state:
                if not min_presses:
                    min_presses = num_presses + min_val
                else:
                    min_presses = min(min_presses, num_presses + min_val)
            if is_valid:
                queue.append((tuple(new_state), num_presses + min_val))
    return min_presses

total = 0
count = 0
for line in sys.stdin:
    re_match = re.search("([\(\d,?+\) ]+) \{([\(\d,?+\) ]+)\}", line.strip())
    buttons = re_match.group(1).strip().replace("(", "").replace(")", "").split(" ")
    for i in range(0, len(buttons)):
        buttons[i] = [int(button) for button in buttons[i].split(",")]
    goal_state = re_match.group(2)
    goal_state = [int(joltage) for joltage in goal_state.split(",")]
   
    new_total = bfs(goal_state, buttons)
    print(new_total)
    total += new_total
    count += 1

print(total)
