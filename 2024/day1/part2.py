left = []
right = []

with open("input.txt") as file:
    for line in file:
        line_arr = line.rstrip().split("  ")
        left.append(int(line_arr[0]))
        right.append(int(line_arr[1]))
 
left = set(left)

sum = 0

for l in left:
    sum += (l * right.count(l))

print(sum)