import re

total = 0

matrix = []
problems = []

with open("input.txt") as file:
    for line in file:
        matrix.append(line.replace('\n',''))

operations = matrix.pop()
matrix.insert(0, operations)
    
width = len(matrix[0])
height = len(matrix)
new_problem = []
new_operand = ""

for i in range(width):
    is_separator = True
    for j in range(height):
        #print(f"matrix[{j}][{i}]:{matrix[j][i]}")
        if matrix[j][i] != ' ':
            is_separator = False
            if matrix[j][i] == '+' or matrix[j][i] == '*':
                new_problem.append(matrix[j][i])
            else:
                new_operand += matrix[j][i]
    if is_separator:
        #print("separated")
        is_separator = True
        problems.append(new_problem)
        new_problem = []
    else:
        #print(f"operand: {new_operand}")
        new_problem.append(new_operand)
        new_operand = ""
problems.append(new_problem)

#print(matrix)
#print(problems)

for i,problem in enumerate(problems):
    operation = problem[0]
    result = 0
    if operation == '*':
        result = 1
        for operand in problem[1:]:
            result = int(result) * int(operand)
    else:
        for operand in problem[1:]:
            result = result + int(operand)
    total += result

            
print(f"Final: {total}")
