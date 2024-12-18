
left = []
right = []

with open("input.txt") as file:
    for line in file:
        line_arr = line.rstrip().split("  ")
        left.append(line_arr[0])
        right.append(line_arr[1])

left.sort()
right.sort()

sum = 0

for l,r in zip(left,right):
    sum += abs(int(l)-int(r))

print(sum)