from math import factorial
n = int(input("enter no.of rows"))
for i in range(n):
   for space in range(1,n-i):
      print(end=" ")
   for j in range(i+1):
      ncr = factorial(i)//(factorial(j)*factorial(i-j))
      print(ncr,end=" ")
   print(" ")
