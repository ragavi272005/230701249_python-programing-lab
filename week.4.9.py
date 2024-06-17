N = int(input())
temp = N
for divisor in range(2, 10):
while temp % divisor == 0:
temp //= divisor
if temp == 1:
print("Yes")
else:
print("No")
