def remove_common(a,b):
common = list(set(a) - set(b))
common1 = list(set(b) - set(a))
common3 = common+common1
if len(common3) > 0:
for i in range(len(common3)):
print(common3[i],'',end='')
print('')
print(len(common3))
else:
print('NO SUCH ELEMENTS')
num = input()
a = set (map(int,input().split()))
b = set (map(int,input().split()))
remove_common(a,b)
