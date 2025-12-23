import sys
import re

def bfs(goal_state, buttons):
    queue = []
    cur_state = '.' * len(goal_state)
    for button in buttons:
        queue.append((button, cur_state, 0))
    while True:
        button, cur_state, num_presses = queue.pop(0)
        new_state = ""
        for i in range(len(cur_state)):
            if i in button:
                if cur_state[i] == '.':
                    new_state += '#'
                else:
                    new_state += '.'
            else:
                new_state += cur_state[i]
        if new_state == goal_state:
            return num_presses + 1
        for button in buttons:
            queue.append((button, new_state, num_presses + 1))
            

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
    
