n = int(input())
p = int(input())
factors = []
for i in range(1, int(n**0.5) + 1):
if n % i == 0:
factors.append(i)
if i != n // i:
factors.append(n // i)
factors.sort()
if p <= len(factors):
print(factors[p-1])
else:
print(0)
