total = 0


def contains_repeat(number: str) -> bool:
    half = int(len(number) / 2)
    half_1 = number[half:]
    half_2 = number[:half]
    return half_1 == half_2
        

with open("input.txt") as file:
    for id_range in file.readline().split(','):
        range_start = int(id_range.split('-')[0])
        range_end = int(id_range.split('-')[1]) + 1
        print(f"start:{range_start}\tend:{range_end}")
        for id in range(range_start, range_end):
            id_str = str(id)
            if all(char == id_str[0] for char in id_str) and (len(id_str) not in [1,3,5,7]):
            #if len(id_str) % 2 != 0:
                #print(f"{id} -> Invalid")
                total += id
                continue
            if contains_repeat(id_str):
                #print(f"{id} -> Invalid")
                total += id
            #else:
            #    print(f"{id}")
            
print(f"Final: {total}")
