t = tuple(map(int,input().split(',')))
inp = int(input())
s=set(t)
count = 0
for x in s:
if inp - x in s:
count += 1
res = count // 2
print(res)
