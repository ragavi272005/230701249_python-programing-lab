n = int(input("Enter the size of the array: "))
arr = []
for i in range(n):
element = int(input(f"Enter element {i+1} of {n}: "))
arr.append(element)
total_sum = sum(arr)
left_sum = 0
pivot_index = -1
for i in range(n):
total_sum -= arr[i]
if left_sum == total_sum:
pivot_index = i
break
left_sum += arr[i]
print(f"The index of the pivot is: {pivot_index}")
