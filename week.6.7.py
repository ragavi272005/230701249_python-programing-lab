s = input()
alphabets = [c for c in s if c.isalpha()]
reversed_alphabets = alphabets[::-1]
result_list = []
j = 0
for i in range(len(s)):
if s[i].isalpha():
result_list.append(reversed_alphabets[j])
j += 1
else:
result_list.append(s[i])
result = ''.join(result_list)
print(result)
