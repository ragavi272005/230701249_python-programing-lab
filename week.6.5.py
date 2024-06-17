s = input()
words = s.split()
non_palindromes = []
for word in words:
if word.lower() != word.lower()[::-1]:
non_palindromes.append(word)
result = ' '.join(non_palindromes)
print(result)
