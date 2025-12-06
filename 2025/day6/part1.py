total = 0

matrix = []
problems = []

with open("input.txt") as file:
    for line in file:
        matrix.append(line.split())

width = len(matrix[0])
height = len(matrix)

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
