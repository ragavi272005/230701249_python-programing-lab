n = int(input())
term = 0
sum_of_series = 0
for i in range(1, n+1):
term = term * 10 + 1
sum_of_series += term
print(sum_of_series)
