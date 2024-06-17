num = int(input()) mask = 1
count = 0

count += num & mask num >>= 1
count += num & mask num >>= 1
count += num & mask num >>= 1
count += num & mask num >>= 1 
print(count)
