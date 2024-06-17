arr = []
for i in range(n):
element = int(input())
arr.append(element)
arr.sort()
processed = []
for i in range(n):
if arr[i] not in processed:
count = arr.count(arr[i])
print(f"{arr[i]} occurs {count} times")
processed.append(arr[i])
