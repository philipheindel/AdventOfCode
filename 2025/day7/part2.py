total = 0

debugging = True

if debugging:
    input_file = "test_input.txt"
else:
    input_file = "input.txt"


matrix = []
splits = 0
paths = 0


def debug(message: str, end: str = '\n') -> None:
    global debugging
    if debugging:
        print(message, end=end)



def eval_point(row: int, col: int) -> None:
    global matrix
    global splits
    current_point = matrix[row][col]
    previous_point = matrix[row-1][col]
    if col-1 >= 0:
        current_left = matrix[row][col-1]
    if col+1 < len(matrix[row]):
        current_right = matrix[row][col+1]
    if current_point == "." and (previous_point == "." or previous_point == "^"):
        return
    if current_point == "." and previous_point == "|":
        matrix[row][col] = "|"
        return
    if current_point == "^" and previous_point == "|":
        if current_left == "." or current_right == ".":
            debug(f"matrix[{row}][{col}] = {matrix[row][col]}")
            splits += 1
            matrix[row][col-1] = "|"
            matrix[row][col+1] = "|"
            matrix[row][col] = "+"
    if previous_point == "S":
        matrix[row][col] = "|"
        return


with open(input_file) as file:
    for line in file:
        matrix.append(list(line.rstrip()))

for i,row in enumerate(matrix):
    for j,element in enumerate(matrix[i]):
        eval_point(i, j)
    # print(matrix[i])

for i,row in enumerate(matrix):
    for j,element in enumerate(matrix[i]):
        debug(matrix[i][j], "")
    debug("")

total = splits

print(f"Final: {total}")
