total = 0

matrix = []

def check_row(row: int, col: int) -> int:
    count = 0
    if row < 0 or row >= len(matrix):
        return count
    if matrix[row][col] == "@" or matrix[row][col] == "X":
        count += 1
    #    print("@",end='')
    #else:
    #    print(".",end='')
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


def clean_grid():
    global total
    for i,row in enumerate(matrix):
        for j,element in enumerate(row):
            if matrix[i][j] == "X":
                matrix[i][j] = "."
                total += 1


def get_removable() -> int:
    removable_count = 0
    for i,row in enumerate(matrix):
        for j,element in enumerate(row):
            if element == ".":
                #print(".",end='')
                continue
            adjacent_count = check_row(i+1,j)
            adjacent_count += (check_row(i,j) - 1)
            adjacent_count += check_row(i-1,j)
            if adjacent_count < 4:
                removable_count += 1
                matrix[i][j] = "X"
    return removable_count
    

with open("input.txt") as file:
    for line in file:
        matrix.append(list(line.rstrip()))
    
while True:
    clean_grid()
    
    removable = get_removable()
    
    if removable == 0:
        break
            
print(f"Final: {total}")
