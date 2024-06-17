from operator import itemgetter
num = int(input())
students = []
for i in range(num):
name, test, assgn, lab = input().split(" ")
test, assgn, lab = int(test), int(assgn), int(lab)
students.append({"name": name, "test": test, "assgn": assgn, "lab": lab, "avg" : (test +
assgn + lab) / 3})
def get_names(items, field, comp):
return sorted([i["name"] for i in items if i[field] == comp(items,
key=itemgetter(field))[field]])
print(*get_names(students, "avg", max))
print(*get_names(students ,"assgn", max))
print(*get_names(students, "lab", min))
print(*get_names(students, "avg", min))
