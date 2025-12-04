total = 0


def get_max_joltage(number: str, digits: int) -> int:
    final = ""
    print(f"> {number}")
    upper_limit = -1
    start_index = digits
    for i in range(len(number[digits:]), len(number)):
        current_largest = int(number[i])
        current_index = i
        for j in range(i, upper_limit , -1):
            current = int(number[j])
            if current >= current_largest:
                current_largest = current
                current_index = j
        upper_limit = current_index
        final += str(current_largest)
        print(f"j:{j} i:{i} {current_largest}")
    print(f"inal")
    return int(final)


with open("input.txt") as file:
    for line in file:
        total += get_max_joltage(line.rstrip(), 12)


print(f"Final: {total}")
