def mergeSort(myList):
if len(myList) > 1:
mid = len(myList) // 2
left = myList[:mid]
right = myList[mid:]
mergeSort(left)
mergeSort(right)
i=0
j=0
k=0
while i < len(left) and j< len(right):
if left[i] <= right[j]:
myList[k]=left[i]
i=i+1
else:
myList[k]=right[j]
j+=1
k+=1
while i < len(left):
myList[k]=left[i]
i+=1
k+=1
while j < len(right):
myList[k]=right[j]
j+=1
k+=1
n=int(input())
input_string=input()
list=input_string.split()
for i in range(len(list)):
list[i]=int(list[i])
#print(list)
mergeSort(list)
for i in range(len(list)):
print(list[i],end='')
print(' ',end='')
