import numpy as np

total = 0

ranges = []
fresh_ids =[]

with open("test_input.txt") as file:
    for line in file:
        if line.rstrip() == "":
            break
        range_start = int(line.rstrip().split('-')[0])
        range_end = int(line.rstrip().split('-')[1])
        ranges.append([range_start, range_end])

ranges = sorted(ranges, key=lambda x: x[0])
merged_ranges = []
i = 0
j = i + 1
current_range = [ranges[0][0],ranges[0][1]]
while i < len(ranges):
    if j >= len(ranges):
        break
    current_start = ranges[i][0]
    current_end = ranges[i][1]
    next_start = ranges[j][0]
    next_end = ranges[j][1]
    print(f"i: {i}, j: {j}")
    print(f"cs: {current_start}, ce: {current_end}\n ns: {next_start}, ne: {next_end}")
    if current_end < next_start:
        print(f"{current_end} < {next_start}")
        i = j
        j = i + 1
        merged_ranges.append(current_range)
        print(current_range)
        current_range = [0,0]
        # move on to next range
        # update i and j indices 
        continue
    if current_end >= next_start:
        print(f"{current_end} >= {next_start}")
        current_range[0] = current_start
        current_range[1] = next_end
        
        j += 1
        # merge current and next
        # update j index
        print(current_range)
        continue

print(merged_ranges)


total = len(fresh_ids)


print(f"Final: {total}")