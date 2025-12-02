left = []
right = []
location = 50
zero_count = 0

with open("input.txt") as file:
    for line in file:
        start = location
        print(f"start: {location}; new: {line}")
        direction = int(1) if line[0] == "R" else int(-1)
        amount = int(line[1:])
        new_location = location + (amount * direction)
        print(f"new_location: {new_location}")
        if new_location == 0 or new_location == 100:
            zero_count += 1
            location = 0
        elif new_location < 0:
            location = 100 + new_location
        elif new_location > 100:
            location = new_location - 100
        else:
            location = new_location
        print(f"final: {location}")


print(zero_count)