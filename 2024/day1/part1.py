$
  2 left = []$
  3 right = []$
  4 $
  5 with open("input.txt") as file:$
  6     for line in file:$
  7         line_arr = line.rstrip().split("  ")$
  8         left.append(line_arr[0])$
  9         right.append(line_arr[1])$
 10 $
 11 left.sort()$
 12 right.sort()$
 13 $
 14 sum = 0$
 15 $
 16 for l,r in zip(left,right):$
 17     sum += abs(int(l)-int(r))$
 18 $
 19 print(sum)$