import sys
import heapq

positions = []

for line in sys.stdin:
    positions.append(tuple(int(num) for num in line.split(",")))

heap = []

for i in range(0, len(positions)):
    for j in range(i + 1, len(positions)):
        pos1 = positions[i]
        pos2 = positions[j]
        distance = 0
        for coord1, coord2 in zip(pos1, pos2):
            distance += (coord2 - coord1) ** 2
        distance = distance ** 0.5
        heapq.heappush(heap, (distance, pos1, pos2))

circuits = []

for i in range(0, 1000):
    item = heapq.heappop(heap)
    pos1 = item[1]
    pos2 = item[2]
    added = []
    for circuit_ind, circuit in enumerate(circuits):
        if pos1 in circuit or pos2 in circuit:
            circuit.add(pos1)
            circuit.add(pos2)
            added.append(circuit_ind)
    if not added:
        circuits.append(set())
        circuits[-1].add(pos1)
        circuits[-1].add(pos2)
    if len(added) > 1:
        dest = added[0]
        for ind in added[1:]:
            circuits[dest] |= circuits[ind]
        for ind in added[1:]:
            del circuits[ind]
        
        


max_heap = []
for circuit in circuits:
    heapq.heappush(max_heap, -len(circuit))

total = 1
for i in range(3):
    length = -heapq.heappop(max_heap)
    print(length)
    total *= length

print(total)
    
