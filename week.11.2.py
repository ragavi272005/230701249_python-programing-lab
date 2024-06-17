try:
user_input = input("Please enter a number between 1 and 100: ").strip()
number = int(user_input)
if 1 <= number <= 100:
print("Valid input.")
else:
print("Error: Number out of allowed range.")
except ValueError:
print("Error: invalid literal for int()")
