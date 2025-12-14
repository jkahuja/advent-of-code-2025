import sys

ranges = []

for line in sys.stdin:
    if line.strip() == "":
        break
    ranges.append(tuple([int(x) for x in line.strip().split('-')]))

done = False

while not done:
    print("STILL NOT DONE")
    done = True
    combined_ranges = set()
    for i, range_ in enumerate(ranges):
        added_range = False
        for j in range(i + 1, len(ranges)):
            if range_[0] >= ranges[j][0] and range_[1] <= ranges[j][1]:
                combined_ranges.add(ranges[j])
                done = False
                print("combined", range_, ranges[j])
                added_range = True
            elif ranges[j][0] >= range_[0] and ranges[j][1] <= range_[1]:
                combined_ranges.add(range_)
                print("combined", range_, ranges[j])
                done = False
                added_range = True
            elif range_[0] >= ranges[j][0] and range_[1] >= ranges[j][1] and ranges[j][1] >= range_[0]:
                combined_ranges.add((ranges[j][0], range_[1]))
                print("combined", range_, ranges[j])
                done = False
                added_range = True
            elif ranges[j][0] >= range_[0] and ranges[j][1] >= range_[1] and range_[1] >= ranges[j][0]:
                combined_ranges.add((range_[0], ranges[j][1]))
                print("combined", range_, ranges[j])
                done = False
                added_range = True
        if not added_range:
            combined_ranges.add(range_)
    if combined_ranges:
        ranges = list(combined_ranges)

print(ranges)

num_fresh_ids = 0

for range_ in ranges:
    num_fresh_ids += (range_[1] - range_[0]) + 1
        
print(num_fresh_ids)
