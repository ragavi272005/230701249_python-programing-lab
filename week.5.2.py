T = int(input(""))
for _ in range(T):
N = int(input(""))
arr = []
for _ in range(N):
arr.append(int(input("")))
k = int(input(""))
arr_set = set(arr)
found = 0
for num in arr:
if (num - k) in arr_set or (num + k) in arr_set:
found = 1
break
print(found)
