thirtyOnes = ["January", "March", "May", "July", "August", "October", "December"]
month = input().strip()
if month == "February":
  print(f"{month} has 28 or 29 days in it.")
elif month in thirtyOnes:
  print(f"{month} has 31 days in it.")
else:
  print(f"{month} has 30 days in it.")
