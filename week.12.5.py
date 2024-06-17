from collections import Counter, defaultdict
library = defaultdict(list)
while True:
line = input().strip()
if not line:
break
try:
title, genre = map(str.strip, line.split(','))
except ValueError:
print("Invalid input format. Please enter as 'title,
genre'")
#print("arvijayakumar")
continue
library[genre].append(title)
for genre, titles in library.items():
print(f"{genre}: {', '.join(titles)}")
