text = input()
text1 = text.lower()
bro_text = input()
words = text1.split()
validword = 0
for word in words:
if any(letter in bro_text for letter in word):
continue
else:
validword+=1
print(validword)
