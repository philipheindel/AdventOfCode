total = 0


def get_max_joltage(number: str, digits: int) -> int:
    largest = 0
    print(f"{digits}{number}")
    upper_limit = 0
    start_index = digits
    for i in range(len(number[digits:]), len(number)):
        print(number[i])
        for j in range(len(number) - digits, -1, -1):
            print(number[j])
            #print(f"{current}")
            #if current > largest:
            #    largest = current
        print()
    print(f"{largest}")
    return largest


with open("test_input.txt") as file:
    for line in file:
        total += get_max_joltage(line.rstrip(), 2)


print(f"Final: {total}")