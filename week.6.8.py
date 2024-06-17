s1 = input()
s2 = input()
result = True
for char in s1:
if char not in s2:
result = False
break
print("True" if result else "False")
