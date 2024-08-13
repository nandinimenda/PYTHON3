l = []
n = int(input("enter no of elements"))
for i in range(n):
   ele = int(input("enter the elements"))
   ele = l.append(ele)
print(l)
d = int(input("enter element to be removed:"))
l.remove(d)
print(l)
