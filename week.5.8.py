N1 = int(input())
array1 = [int(input()) for _ in range(N1)]
N2 = int(input())
array2 = [int(input()) for _ in range(N2)]
merged_array = sorted(set(array1 + array2))
print(" ".join(map(str, merged_array)))
