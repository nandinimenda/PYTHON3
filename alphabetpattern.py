n = int(input("enter no.of rows"))
A = 65
for i in range(1,n+1):
   for j in range(1,i+1):
      print(chr(A),end=" ")
   A+=1
   print("")
