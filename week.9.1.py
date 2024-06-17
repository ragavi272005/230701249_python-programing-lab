s1 = input().strip()
s2 = input().strip()
word1 = s1.split()
word2 = s2.split()
word_count1 = {}
word_count2 = {}
for word in word1:
word_count1[word] = word_count1.get(word,0) + 1
for word in word2:
word_count2[word] = word_count2.get(word,0) + 1
uncommon_word = set()
for word,count in word_count1.items():
if count == 1 and word not in word_count2:
uncommon_word.add(word)
for word,count in word_count2.items():
if count == 1 and word not in word_count1:
uncommon_word.add(word)
if len(uncommon_word) == 0:
print('No uncommon words')
else:
x=list(uncommon_word)
print(*x)
