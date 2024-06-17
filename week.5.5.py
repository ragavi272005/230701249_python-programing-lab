arr = [None] * 10
print()
for i in range(10):
arr[i] = int(input())
item = int(input())
print(f"ITEM to be inserted: {item}")
position = 0
while position < len(arr) and arr[position] < item:
position += 1
arr.append(None)
for i in range(len(arr) - 1, position, -1):
arr[i] = arr[i-1]
arr[position] = item
print("After insertion array is:")
for element in arr:
print(element)
