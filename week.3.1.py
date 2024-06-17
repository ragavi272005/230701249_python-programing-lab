m, p, c = int(input()), int(input()), int(input())
if m + p + c >= 180 or (m >= 65 and p >= 55 and c >= 50):
   print("The candidate is eligible")
else:
   print("The candidate is not eligible")
