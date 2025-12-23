import sys
import re
import copy

def bfs(goal_state, buttons):
    visited = set()
    queue = []
    cur_state = '.' * len(goal_state)
    for button in buttons:
        queue.append((button, cur_state, 0))
    while True:
        cur_button, cur_state, num_presses = queue.pop(0)
        new_state = ""
        for i in range(len(cur_state)):
            if i in cur_button:
                if cur_state[i] == '.':
                    new_state += '#'
                else:
                    new_state += '.'
            else:
                new_state += cur_state[i]
        if new_state == goal_state:
            return num_presses + 1
        for new_button in buttons:
            if new_button == cur_button:
                continue
            if ((tuple(new_button), new_state, num_presses + 1)) in visited:
                continue
            queue.append((new_button, new_state, num_presses + 1))
            visited.add((tuple(new_button), new_state, num_presses + 1))
            

total = 0
count = 0
for line in sys.stdin:
    re_match = re.search("\[([\.|\#]+)\] ([\(\d,?+\) ]+)", line.strip())
    goal_state = re_match.group(1)
    buttons = re_match.group(2).strip().replace("(", "").replace(")", "").split(" ")
    for i in range(0, len(buttons)):
        buttons[i] = [int(button) for button in buttons[i].split(",")]
    
    total += bfs(goal_state, buttons)
    count += 1
    print("TOTAL = ", total)
    print("count = ", count)

print(total)
    
