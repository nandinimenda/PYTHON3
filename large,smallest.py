def max_min(numbers):
   largest = max(numbers)
   smallest = min(numbers)
   return largest,smallest
numbers = [2,6,3,8,4]
largest,smallest = max_min(numbers)
print(largest)
print(smallest)
