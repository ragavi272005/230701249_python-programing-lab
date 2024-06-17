def digit_difference(num_str):
even_sum = 0
odd_sum = 0
for i, digit in enumerate(num_str):
if i % 2 == 0:
even_sum += int(digit)
else:
odd_sum += int(digit)
return abs(even_sum - odd_sum)
