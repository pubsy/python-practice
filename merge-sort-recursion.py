
def divide(arr):
  n = len(arr)
  if n == 1:
    return arr
  a = divide(arr[0 : n/2])
  b = divide(arr[n/2 : n])
  return merge(a,b)
    

def merge(a, b):
  result = []
  k = 0
  i = 0
  j = 0
  while k < len(a) + len(b):
    if i == len(a) and j == len(b):
      break;
    elif i == len(a) and j < len(b):
      result.append(b[j])
      j += 1
    elif j == len(b) and i < len(a):
      result.append(a[i])
      i += 1
    elif a[i] <= b[j]:
      result.append(a[i])
      i += 1
    else:
      result.append(b[j])
      j += 1
    k += 1
  return result

sorted = divide([7,2,4,6])

for val in sorted:
  print(val)
