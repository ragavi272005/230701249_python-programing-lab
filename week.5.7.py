m = int(input())
n = int(input())
list1 = []
list2 = []
for _ in range(m):
row = [int(input()) for _ in range(n)]
list1.append(row)
for _ in range(m):
row = [int(input()) for _ in range(n)]
list2.append(row)
zipped_list = [list1[i] + list2[i] for i in range(m)]
print("Zipped List:", zipped_list)
