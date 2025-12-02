location = 50
zero_count = 0

with open("input.txt") as file:
    for line in file:
        start = location
        direction = int(1) if line[0].rstrip() == "R" else int(-1)
        amount = line[1:].rstrip()
        if len(amount) > 2:
            amount = int(amount[-2:])
        else:
            amount = int(amount)
        new_location = location + (amount * direction)
        if new_location == 0 or new_location == 100:
            zero_count += 1
            location = 0
        elif new_location < 0:
            location = 100 + new_location
        elif new_location > 100:
            location = new_location - 100
        else:
            location = new_location
        print(f"{start} +\t{(amount * direction)}\t= {location}")


print(f"Final: {zero_count}")
