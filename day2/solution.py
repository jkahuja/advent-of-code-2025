import sys

total = 0

line = sys.stdin.read()
ranges = line.split(',')
for range_ in ranges:
    start, end = range_.split('-')
    start = int(start)
    end = int(end)
    for i in range(start, end + 1):
        str_num = str(i)
        split_point = int(len(str_num) / 2)
        if str_num[0:split_point] == str_num[split_point:]:
            total += i

print(total) 
             
    
