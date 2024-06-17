def productDigits(n):
num = str(n)
even = 1
odd = 0
for i,digit in enumerate(num):
digit = int(digit)
if(i+1)%2 == 0:
even *= digit
else:
odd += digit
return even % odd == 0
