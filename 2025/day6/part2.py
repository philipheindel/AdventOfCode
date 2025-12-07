import re

total = 0

matrix = []
problems = []

with open("test_input.txt") as file:
    for line in file:
        matrix.append(line.replace('\n',''))

operations = matrix.pop()
matrix.insert(0, operations)
    
width = len(matrix[0].split())
height = len(matrix)

for i in range(width):
    is_separator = True
    for j in range(height):
        if matrix[j][i] != ' ':
            is_separator = False
    if is_separator:

        print(f"{j} {i}")

print(matrix)

exit()
for i in range(width):
    new_problem = []
    for j in range(height):
        new_problem.append(matrix[j][i])
    problems.append(new_problem)

for i,problem in enumerate(problems):
    problem.reverse()
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
