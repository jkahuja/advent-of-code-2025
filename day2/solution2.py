import sys

total = 0


def is_duplicate(str_num, split_point, key):
    if len(str_num) == 0:
        return True
    return str_num[0:split_point] == key and is_duplicate(
        str_num[split_point:], split_point, key
    )


line = sys.stdin.read()
ranges = line.split(",")
for range_ in ranges:
    start, end = range_.split("-")
    start = int(start)
    end = int(end)
    for i in range(start, end + 1):
        str_num = str(i)
        for num_splits in range(2, int(len(str_num)) + 1):
            if len(str_num) % num_splits != 0:
                continue
            split_point = int(len(str_num) / num_splits)
            if is_duplicate(str_num, split_point, str_num[0:split_point]):
                total += i
                break

print(total)
