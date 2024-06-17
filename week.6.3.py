S1 = input()
S2 = input()
N = int(input())
result = ''
for char in S1:
if char in S2 and char not in result:
result += char
if len(result) == N:
break
print(result)
