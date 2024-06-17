n = int(input())
print()
lst = [int(input()) for _ in range(n)]
target = int(input())
count = 0
location = 1
for element in lst:
if element == target:
print(f"Element found at location: {location}")
count += 1
location += 1
if count > 0:
print(f"Total occurrences of the element: {count}")
else:
print(f"{target} is not present in the array.")
