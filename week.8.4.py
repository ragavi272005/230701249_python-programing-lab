n = list(map(int,input().split()))
n_set=set()
for num in n:
if num in n_set:
print(num)
break
else:
n_set.add(num)
