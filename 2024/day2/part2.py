
def is_safe(report, index, direction, dampened):
    if index == (len(report) - 1):
        return True
    
    curr_dmp = dampened
    curr_val = int(report[index])
    next_val = int(report[index + 1])
    curr_dir = direction
    next_dir = 0
    print(f"ix:{index} dp: {dampened} cv:{curr_val} nv:{next_val} cd:{direction} nd:{next_dir}")

    if curr_val == next_val:
        if not dampened:
            print("dampening")
            dampened = True
        else:
            return False
    
    if curr_val > next_val:
        next_dir = 1
    elif curr_val < next_val:
        next_dir = 2

    if direction == 0:
        curr_dir = next_dir

    if curr_dir != next_dir:
        if not dampened:
            print("dampening")
            dampened = True
        else:
            return False

    if abs(int(curr_val) - int(next_val)) > 3:
        if not dampened:
            print("dampening")
            del report[index]
            dampened = True
        else:
            return False

    return is_safe(report, index + 1, next_dir, dampened)

def load_input(input_file, per_line_separator):
    file_array = []
    with open(input_file) as file:
        for line in file:
            file_array.append(line.rstrip().split(per_line_separator))
    return file_array

reports = load_input("input.txt", " ")

sum = 0

for report in reports:
    print(report)
    if is_safe(report, 0, 0, False):
        sum += 1
        print("safe")

print(sum)