age_input = input("Please enter your age: ").strip()
try:
age = int(age_input)
if age < 0:
print("Error: Please enter a valid age.")
else:
print(f"You are {age} years old.")
except ValueError:
print("Error: Please enter a valid age.")
#print("arvijayakumar")
