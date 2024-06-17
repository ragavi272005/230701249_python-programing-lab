s = input()
s_count = {}
for i in range (len(s)-9):
substring = s[i:i+10]
s_count[substring] = s_count.get(substring,0)+1
rep_string = [substring for substring,count in s_count.items() if count > 1]
for i in rep_string:
print(i)
