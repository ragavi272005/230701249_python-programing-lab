n=int(input())
ele=input()
ele1=ele.split()
for i in range(len(ele1)):
ele1[i]=int(ele1[i])
s_count=0
for i in range(n-1):
for j in range(0,n-i-1):
if ele1[j]>ele1[j+1]:
s_count=s_count+1
ele1[j],ele1[j+1]=ele1[j+1],ele1[j]
print('List is sorted in',s_count,'swaps.')
print('First Element:',ele1[0])
print('Last Element:',ele1[n-1])
