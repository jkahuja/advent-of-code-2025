import sys

total = 0

def find_max(arr):
    max_num = arr[0]
    max_ind = 0
    for idx, num in enumerate(arr[1:]):
        if num > max_num:
            max_num = num
            max_ind = idx + 1
    return str(max_num), max_ind + 1
     

for line in sys.stdin:
    arr = [int(ch) for ch in line.strip()]
    cur_str = ""
    start = 0
    for i in range(0, 12):
        max_ch, new_start = find_max(arr[start:len(arr) - (12 - i) + 1])
        cur_str += max_ch
        start += new_start
    total += int(cur_str)

print(total)
