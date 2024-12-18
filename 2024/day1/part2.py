left = []$
  3 right = []$
  4 $
  5 with open("input.txt") as file:$
  6     for line in file:$
  7         line_arr = line.rstrip().split("  ")$
  8         left.append(int(line_arr[0]))$
  9         right.append(int(line_arr[1]))$
 10 $
 11 left = set(left)$
 12 $
 13 sum = 0$
 14 $
 15 for l in left:$
 16     sum += (l * right.count(l))$
 17 $
 18 print(sum)