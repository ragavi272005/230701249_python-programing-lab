def binary_search(arr,low,high,x):
if high >= low:
mid=(low + high)
if arr[mid]==x:
return mid
elif arr[mid]> x:
return binary_search(arr,low,mid-1,x)
else:
return binary_search(arr,mid+1,high,x)
else:
return -1
input_string=input()
list=input_string.split(",")
for i in range(len(list)):
list[i]=int(list[i])
x=int(input())
result=binary_search(list,0,len(list)-1,x)
if result!=-1:
print('True')
else:
print('False')
