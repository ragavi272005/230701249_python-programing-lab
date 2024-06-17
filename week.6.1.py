input_string = input()
letters = digits = special_symbols = 0
for char in input_string:
if char.isalpha():
letters += 1
elif char.isdigit():
digits += 1
else:
special_symbols += 1
print(letters)
print(digits)
print(special_symbols)
