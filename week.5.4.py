n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
element = int(input(f"Enter element {i+1}: "))
arr.append(element)
arr.sort()
prev_element = None
for element in arr:
if element != prev_element:
print(element, end=" ")
prev_element = element
