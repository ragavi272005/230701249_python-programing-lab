s = input()
s_list = list(s)
i = 0
while i < len(s_list):
if s_list[i].isdigit():
num_str = s_list[i]
i += 1
while i < len(s_list) and s_list[i].isdigit():
num_str += s_list[i]
i += 1
repeat_times = int(num_str) - 1
s_list[i-len(num_str):i] = [s_list[i-len(num_str)-1]] * repeat_times
else:
i += 1
decompressed_string = ''.join(s_list)
print(decompressed_string)
