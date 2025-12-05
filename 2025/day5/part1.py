total = 0


ranges = []
ids = []


with open("input.txt") as file:
    range_mode = True
    for line in file:
        if line.rstrip() == "":
            range_mode = False
            continue
        if range_mode:
            range_start = int(line.rstrip().split('-')[0])
            range_end = int(line.rstrip().split('-')[1])
            ranges.append([range_start, range_end])
        else:
            ids.append(int(line.rstrip()))


for ingredient_id in ids:
    for fresh_range in ranges:
        if ingredient_id in range(fresh_range[0], fresh_range[1] + 1):
            total += 1
            break


print(f"Final: {total}")
