def is_binary_string(s):
s = set(s)
l = sorted(s)
if( len(l)==2 and l[0]==’0’ and l[1]==’1’):
return “Yes”
else:
return “No”
