N = int(input())
temp = N
num_digits = 0
while temp > 0:
num_digits += 1
temp //= 10
sum_of_powers = 0
temp = N
while temp > 0:
digit = temp % 10
sum_of_powers += digit ** num_digits
num_digits -= 1
temp //= 10
if sum_of_powers == N:
print("The number is a Disarium number.")
else:
print("The number is not a Disarium number.")
