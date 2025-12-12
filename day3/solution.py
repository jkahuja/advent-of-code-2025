import sys

total = 0

for line in sys.stdin:
    arr = [int(ch) for ch in line.strip()]
    max_num = arr[0]
    max_ind = 0
    for idx, num in enumerate(arr[1:-1]):
        if num > max_num:
            max_num = num
            max_ind = idx + 1
    second_max_ind = max_ind + 1
    second_max_num = arr[second_max_ind]
    for num in arr[second_max_ind + 1 :]:
        second_max_num = max(second_max_num, num)
    total += int(str(max_num) + str(second_max_num))


print(total)
