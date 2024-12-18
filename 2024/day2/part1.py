reports = []

with open("input.txt") as file:
    for line in file:
        reports.append(line.rstrip().split(" "))

def is_consistent_change(report):
    direction = 0
    report_iter = iter(report)
    next(report_iter, None)
    for value in report:
        new_direction = 0
        next_value = next(report_iter, None)
        #print(next_value)
        if next_value == None:
            return True

        if value > next_value:
            new_direction = 1
        elif value < next_value:
            new_direction = 2
        else:
            print("dup val")
            return False

        if direction == 0:
            direction = new_direction

        if direction != new_direction:
            print(direction)
            print(new
            print("dir chg")
            return False


def is_small_change(report):
    report_iter = iter(report)
    for value in report:
        next_value = next(report_iter, None)
        if next_value == None:
            return True

        if abs(int(value) - int(next_value)) > 2:
            return False



sum = 0

for report in reports:
    print(report)
    if is_consistent_change(report):# and is_small_change(report):
        sum += 1
        print("safe")
    else:
        print("unsafe")

print(sum)