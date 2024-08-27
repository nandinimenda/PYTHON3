def gcd(a,b):
    if(a==0):
        return b
    if(b==0):
        return a
    if(a==b):
        return a
    if(a>b):
        return gcd(a-b,b)
    return gcd(a,b-a)
a = 20
b = 48
if(gcd(a,b)):
   print(gcd(a,b))
else:
   print("Not found")
