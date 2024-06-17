def checkUgly(n):
if n==1:
return 'ugly'
if n==0:
return 'not ugly'
if ( n % 2 == 0 ):
return checkUgly(n // 2)
if ( n % 3 == 0 ):
return checkUgly(n // 3)
if ( n % 5 == 0 ):
return checkUgly(n // 5)
return 'not ugly'
