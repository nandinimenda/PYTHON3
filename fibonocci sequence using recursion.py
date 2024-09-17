def rfib(n):
   if n<=1:
      return n
   else:
      return (rfib(n-1)+rfib(n-2))
a = int(input())
if a<=0:
   print("enter a positive number")
else:
   print("Fibonnaci series:")
   for i in range(a):
      print(rfib(i))
