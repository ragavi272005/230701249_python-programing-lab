def automorphic(inp):
sq=inp*inp
last=sq%(10**len(str(inp))
if inp==last:
return "Automorphic"
else:
return "Not Automorphic"
