total = 0


ranges = []
fresh_ids =[]


with open("input.txt") as file:
    for line in file:
        if line.rstrip() == "":
            break
        range_start = int(line.rstrip().split('-')[0])
        range_end = int(line.rstrip().split('-')[1]) + 1
        ranges.append([range_start, range_end])
        comb = set(list(fresh_ids), list(range(range_start, range_end)))
        fresh_ids = list(comb)
        continue
        for fresh_id in range(range_start, range_end):
            if fresh_id not in fresh_ids:
                fresh_ids.append(fresh_id)


total = len(fresh_ids)


print(f"Final: {total}")
