total = 0

debugging = True

if debugging:
    input_file = "test_input.txt"
else:
    input_file = "input.txt"


matrix = []


def debug(message: str) -> None:
    global debugging
    if debugging:
        print(message)


def eval_point(row: int, col: int) -> None:
    global matrix
    current_point = matrix[row][col]
    previous_point = matrix[row-1][col]
    if matrix[row][col] == "." or matrix[row][col] == "^":
        if matrix[row-1][col] == "." or matrix[row-1][col] == "^":
            return
        elif matrix[row-1][col] == "|":

    if col-1 >= 0 and (matrix[row][col-1] == "@" or matrix[row][col-1] == "X"):
        count += 1
    #    print("@",end='')
    #else:
    #    print(".",end='')
    if col+1 < len(matrix[row]) and (matrix[row][col+1] == "@" or matrix[row][col+1] == "X"):
        count += 1
    #    print("@")
    #else:
    #    print(".")
    return count



with open(input_file) as file:
    for line in file:
        matrix.append(list(line.rstrip()))

for i,row in enumerate(matrix):
    for j,element in enumerate(row):
        eval_point(i, j)
        if element == ".":
            debug(".",end='')
            continue
        adjacent_count = check_row(i+1,j)
        adjacent_count += (check_row(i,j) - 1)
        adjacent_count += check_row(i-1,j)
        if adjacent_count < 4:
            removable_count += 1
            matrix[i][j] = "X"


print(f"Final: {total}")
