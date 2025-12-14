import sys

ranges = []
ingredients = []
num_fresh = 0

for line in sys.stdin:
    if line.strip() == "":
        break
    ranges.append([int(x) for x in line.strip().split('-')])

for line in sys.stdin:
    ingredients.append(int(line.strip()))

for ingredient in ingredients:
    for range_ in ranges:
        if ingredient >= range_[0] and ingredient <= range_[1]:
            num_fresh += 1
            break

print(num_fresh)
    
