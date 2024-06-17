N = int(input())
non_repeated_count = 0
for digit in range(10):
   found = False
   repeat = False
   temp = N
   while temp > 0:
     current_digit = temp % 10
     if current_digit == digit:
        if found:
          repeat = True
          break
        found = True
    temp //= 10
   if found and not repeat:
    non_repeated_count += 1
print(non_repeated_count)
