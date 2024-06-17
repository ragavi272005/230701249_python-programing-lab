row1 = set('qwertyuiop')
row2 = set('asdfghjkl')
row3 = set('zxcvbnm')
num_words = int(input())
found = False
for _ in range(num_words):
word = input()
word_lower = word.lower()
if all(char in row1 for char in word_lower) or \
all(char in row2 for char in word_lower) or \
all(char in row3 for char in word_lower):
print(word)
found = True
if not found:
print("No words")
