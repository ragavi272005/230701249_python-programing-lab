try:
numerator_input = input().strip()
numerator = float(numerator_input)
denominator_input = input().strip()
denominator = float(denominator_input)
division_result = numerator / denominator
print(f"Division result: {division_result}")
modulo_result = numerator % denominator
print(f"Modulo result: {modulo_result}")
except ValueError:
print("Error: Non-numeric input provided.")
except ZeroDivisionError:
print("Error: Cannot divide or modulo by zero.")
