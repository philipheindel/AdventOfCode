
def is_safe(report, index, direction):
    if index == (len(report) - 1):
        return True
    
    curr_val = int(report[index])
    next_val = int(report[index + 1])
    curr_dir = direction
    next_dir = 0
    
    if curr_val == next_val:
        return False
    
    if curr_val > next_val:
        next_dir = 1
    elif curr_val < next_val:
        next_dir = 2

    if direction == 0:
        curr_dir = next_dir

    if curr_dir != next_dir:
        return False

    if abs(int(curr_val) - int(next_val)) > 3:
        return False

    return is_safe(report, index + 1, next_dir)

def load_input(input_file, per_line_separator):
    file_array = []
    with open(input_file) as file:
        for line in file:
            file_array.append(line.rstrip().split(per_line_separator))
    return file_array

reports = load_input("input.txt", " ")

sum = 0

for report in reports:
    if is_safe(report, 0, 0):
        sum += 1

print(sum)