
total = 0


def contains_repeat(number: str, parts: int) -> bool:
    half = len(number) / 2
    if parts > half:
        return False
    if len(number) % parts != 0:
        return contains_repeat(number, parts + 1)
    parts_divided = [number[i:i+parts] for i in range(0, len(number), parts)]
    if len(set(parts_divided)) == 1:
        print(parts_divided)
        return True
    return contains_repeat(number, parts + 1)
        

with open("input.txt") as file:
    for id_range in file.readline().split(','):
        range_start = int(id_range.split('-')[0])
        range_end = int(id_range.split('-')[1])
        print(f"start:{range_start}\tend:{range_end}")
        for id in range(range_start, range_end):
            id_str = str(id)
            if all(char == id_str[0] for char in id_str):
                total += id
                continue
            if contains_repeat(id_str, 2):
                #print(f"Adding {id} to total")
                total += id
            
print(f"Final: {total}")
