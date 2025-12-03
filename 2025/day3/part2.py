total = 0


def get_max_joltage(number: str, digits: int) -> int:
    largest = 0
    print(f"{number}")
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            current = int(number[i] + number[j])
            #print(f"{current}")
            if current > largest:
                largest = current
    print(f"{largest}")
    return largest
        

with open("test_input.txt") as file:
    for line in file:
        total += get_max_joltage(line.rstrip())

            
print(f"Final: {total}")
