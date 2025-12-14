import sys

ranges = []

for line in sys.stdin:
    if line.strip() == "":
        break
    ranges.append([int(x) for x in line.strip().split('-')])

ranges = sorted(ranges)
combined_ranges = [ranges[0]]

for cur_range in ranges[1:]:
    prev_range = combined_ranges[-1]
    # does the previous range fully contain the current range
    if prev_range[1] >= cur_range[1]:
        continue
    # does the previous range overlap with the current range
    if prev_range[1] <= cur_range[1] and prev_range[1] >= cur_range[0]: 
        combined_ranges[-1] = [prev_range[0], cur_range[1]]
    else:
        combined_ranges.append(cur_range)

num_fresh_ids = 0

print(combined_ranges)

for cur_range in combined_ranges:
    num_fresh_ids += (cur_range[1] - cur_range[0]) + 1
        
print(num_fresh_ids)
