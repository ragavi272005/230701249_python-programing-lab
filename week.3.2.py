sides = set([int(input()), int(input()), int(input())])
if len(sides) == 1:
   print("That's a equilateral triangle")
elif len(sides) == 2:
   print("That's a isosceles triangle")
else:
   print("That's a scalene triangle")
