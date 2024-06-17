import math
user_input = input("Please enter a number: ").strip()
try:
number = float(user_input)
if number < 0:
print("Error: Cannot calculate the square root of a negative number.")
else:
square_root = math.sqrt(number)
print(f"The square root of {number:.2f} is {square_root:.2f}")
except ValueError:
print(f"Error: could not convert string to float")
