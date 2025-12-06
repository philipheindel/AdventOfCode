

total = 0

ranges = []
fresh_ids =[]

with open("input.txt") as file:
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
        merged_ranges.append([current_range[0], current_range[1]])
        break
    if j == (i + 1):
        #print("initial")
        current_range[0] = ranges[i][0]
        current_range[1] = ranges[i][1]
    next_start = ranges[j][0]
    next_end = ranges[j][1]
    #print(f"i: {i}, j: {j}")
    #print(f"cs: {current_range[0]}, ce: {current_range[1]}\n ns: {next_start}, ne: {next_end}")
    if current_range[1] < next_start:
        #print("current")
        #print(current_range)
        merged_ranges.append([current_range[0], current_range[1]])
        #print("merged")
        #print(merged_ranges)
        i = j
        j = i + 1
        #print(current_range)
        # move on to next range
        # update i and j indices 
        continue
    if current_range[1] >= next_start and current_range[1] < next_end:
        current_range[1] = next_end
    j += 1

print(merged_ranges)

for id_range in merged_ranges:
    total += (id_range[1] - id_range[0] + 1)


print(f"Final: {total}")
