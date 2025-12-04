total = 0

matrix = []

def check_row(row: int, col: int) -> int:
    count = 0
    if row < 0 or row >= len(matrix):
        return count
    if matrix[row][col] == "@":
        count += 1
    #    print("@",end='')
    #else:
    #    print(".",end='')
    if col-1 >= 0 and matrix[row][col-1] == "@":
        count += 1
    #    print("@",end='')
    #else:
    #    print(".",end='')
    if col+1 < len(matrix[row]) and matrix[row][col+1] == "@":
        count += 1
    #    print("@")
    #else:
    #    print(".")
    return count
    
    

with open("input.txt") as file:
    for line in file:
        matrix.append(list(line.rstrip()))
    
    
    for i,row in enumerate(matrix):
        for j,element in enumerate(row):
            if element == ".":
                #print(".",end='')
                continue
            adjacent_count = check_row(i+1,j)
            adjacent_count += (check_row(i,j) - 1)
            adjacent_count += check_row(i-1,j)
            if adjacent_count < 4:
                total += 1
                #print("X",end='')
            #else:
                #print("@",end='')
            #print()
        #print()
            
            
    #print(matrix)
    #for char in line.rstrip():
    #    if char == ".":
    #        print("*",end='')
    #        continue
    #    print(char, end='')
    #print()

            
print(f"Final: {total}")
