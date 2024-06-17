def abundant(n):
div_sum = sum([divisor for divisor in range(1,n) if n % divisor ==0 ])
if div_sum > n:
return 'Yes'
else:
return 'No'
