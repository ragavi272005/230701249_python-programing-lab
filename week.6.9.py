items=[]
while True:
try:
a=input()
if not a:
break
if a not in items:
items.append(a)
except EOFError as e:
break
for i in items:
print(i)
