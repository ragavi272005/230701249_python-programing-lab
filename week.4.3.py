N = int(input())
is_prime = 2
if N == 2:
   is_prime = 2
elif N % 2 == 0:
  is_prime = 1
else:
  for i in range(3, int(N**0.5) + 1, 2):
    if N % i == 0:
       is_prime = 1 # Not prime
       break
print(is_prime)
