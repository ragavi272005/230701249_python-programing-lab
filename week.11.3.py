try:
numerator_input = input("Please enter the numerator: ").strip()
numerator = float(numerator_input)
denominator_input = input("Please enter the denominator: ").strip()
denominator = float(denominator_input)
result = numerator / denominator
print(f"The result of the division is {result:.2f}")
except ValueError:
print("Error: Non-numeric input provided.")
except ZeroDivisionError:
print("Error: Cannot divide by zero.")
