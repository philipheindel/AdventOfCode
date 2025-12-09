total = 0

debugging = False

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


def eval_point(row: int, col: int, mtrx) -> None:
    global splits
    if row == len(mtrx):
        splits += 1
        return
    current_point = mtrx[row][col]
    if current_point == "." or current_point == "S":
        eval_point(row + 1, col, mtrx)
    if current_point == "^":
        eval_point(row + 1, col - 1, mtrx)
        eval_point(row + 1, col + 1, mtrx)
 

with open(input_file) as file:
    for line in file:
        matrix.append(list(line.rstrip()))

starting_row = 0
starting_col = matrix[0].index("S")

eval_point(starting_row, starting_col, matrix)

total = splits

print(f"Final: {total}")
