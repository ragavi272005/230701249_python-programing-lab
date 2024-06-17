weapons = int(input())
soldiers = int(input())
res = weapons % 3 == 0 and soldiers % 2 == 0
print(res)
