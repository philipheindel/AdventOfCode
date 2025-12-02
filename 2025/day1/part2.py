left = []
right = []
location = 50
zero_count = 0

with open("../input.txt") as file:
    for line in file:
        print(line.rstrip())
        start = location
        initial_count = zero_count
        direction = int(1) if line[0].rstrip() == "R" else int(-1)
        amount = line[1:].rstrip()
        if len(amount) > 2:
            passes = int(amount[0])
            amount = int(amount[-2:])
        else:
            passes = 0
            amount = int(amount)
        new_location = location + (amount * direction)
        if new_location == 0 or new_location == 100:
            passes += 1
            location = 0
        elif new_location < 0:
            if start != 0:
                passes += 1
            location = 100 + new_location
        elif new_location > 100:
            passes += 1
            location = new_location - 100
        else:
            location = new_location
        zero_count += passes
        print(f"{start} +\t{(amount * direction)}\t= {location}")
        print(f"{initial_count} +\t{passes} =\t {zero_count}")

        


print(f"Final: {zero_count}")
