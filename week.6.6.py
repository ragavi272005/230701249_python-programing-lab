s = input()
words = s.split()
result = words[1].upper() if len(words) >= 2 else "LESS"
print(result)
