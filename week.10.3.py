n=int(input())
num=input()
a=[]
num1=num.split()
for i in range(len(num1)):
num1[i]=int(num1[i])
if num1[0]>num1[1]:
print(num1[0],end='')
for i in range(1,n-1):
if num1[i]>num1[i-1] and num1[i]>num1[i+1]:
print('',num1[i],end='')
if num1[n-1]>num1[n-2]:
print('',num1[n-1])
