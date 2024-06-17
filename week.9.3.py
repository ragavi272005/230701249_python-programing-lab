try:
T = int(input())
result = {}
for _ in range(T):
key,*values = input().split()
values = list(map(int,values))
sum_value=sum(values)
result[key]=sum_value
sorted_results = dict(sorted(result.items(),key = lambda item: item[1]))
for key, value in sorted_results.items():
print(key,value)
except:
print("No input provided")
