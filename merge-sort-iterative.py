from math import pow, log

arr = [5,2,4,7,1,3,2,6]
n = len(arr)

i = int(round(log(n, 2)))
while i > 0:
  j = 0
  while j < n:
    block_size = int(round(n / pow(2, i)))
    start = j
    middle = start + block_size
    end = middle + block_size
    
    left = []
    k = start
    while k < middle:
      left.append(arr[k])
      k += 1
    
    right = []
    k = middle
    while k < end:
      right.append(arr[k])
      k += 1
    
    #mege left and right
    k = start
    l = 0
    r = 0
    while k < end:
      if l == len(left) and r != len(right):
        arr[k] = right[r]
        r += 1
      elif r == len(right) and l != len(left):
        arr[k] = left[l]
        l += 1
      elif left[l] <= right[r]:
        arr[k] = left[l]
        l += 1
      elif left[l] > right[r]:
        arr[k] = right[r]
        r += 1
      k += 1
    j += 2 * block_size
  i -= 1

i = 0
while i < len(arr):
  print(arr[i])
  i += 1

