s1 = input()
s2 = input()
result = ''
for char in s1:
if char not in s2:
result += char
print(result)
