num = input()
r_num =[]
ran_num = num.split()
for i in range(len(ran_num)):
ran_num[i]=int(ran_num[i])
ran_num.sort()
r_d=list(set(ran_num))
for i in range(len(r_d)):
count=0
for j in range(len(ran_num)):
if r_d[i]==ran_num[j]:
count=count+1
#print("arvijayakumar")
print(r_d[i],end='')
print('',count)
