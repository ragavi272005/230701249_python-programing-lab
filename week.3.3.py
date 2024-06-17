units = eval(input())
bill = 0
if units in range(200):
   bill = units * 1.20
elif units in range(200,400):
   bill = units * 1.50
elif units in range(400,600):
   bill = units * 1.80
else:
   bill = units * 2.00
if bill < 100:
   bill = 100
if bill > 400:
   bill += bill * 0.15
print(f"{bill:.2f}")
