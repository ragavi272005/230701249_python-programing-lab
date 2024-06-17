n = int(input())
list1 = [int(input()) for i in range(n)]
is_strictly_increasing = True
can_be_strictly_increasing = False
violations = 0
last_violation_index = -1
for i in range(n - 1):
if list1[i] >= list1[i + 1]:
violations += 1
last_violation_index = i
is_strictly_increasing = False
if violations > 1:
break
if not is_strictly_increasing and violations == 1:
if last_violation_index == 0 or last_violation_index == n - 2:
can_be_strictly_increasing = True
elif list1[last_violation_index - 1] < list1[last_violation_index + 1] or \
list1[last_violation_index] < list1[last_violation_index + 2]:
can_be_strictly_increasing = True
if is_strictly_increasing or can_be_strictly_increasing:
print("True")
else:
print("False")
