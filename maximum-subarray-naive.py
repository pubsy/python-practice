array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

maxSum = 0
maxI = 0
maxJ = 0

i = 0
while i < len(array):
    j = i
    sum = 0
    while j < len(array):
         sum += array[j]
         if sum >= maxSum:
             maxSum = sum
             maxI = i
             maxJ = j
         j += 1
    i += 1

print(maxSum)
print(maxI)
print(maxJ)
