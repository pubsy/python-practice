array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

def find_max_crossing(left, mid, right, arr):

  max_left = mid 
  curr_max = -1000;

  sum = 0
  i = mid
  while i >= left:
    sum += arr[i]
    if sum >= curr_max:
      curr_max = sum
      max_left = i
    i -= 1
  left_sum = curr_max

  max_right = mid + 1
  curr_max = -1000

  sum = 0
  i = mid + 1
  while i <= right:
    sum += arr[i]
    if sum >= curr_max:
      curr_max = sum
      max_right = i
    i += 1
  right_sum = curr_max

  return(max_left, max_right, left_sum + right_sum)

def find_max_subarray(left, right, arr):
  if left == right:
    return (left, right, arr[left])
  mid = (left + right)/2
  left_low, left_high, left_sum = find_max_subarray(left, mid, arr)
  right_low, right_high, right_sum = find_max_subarray(mid + 1, right, arr)
  cross_low, cross_high, cross_sum = find_max_crossing(left, mid, right, arr)
  if left_sum >= right_sum and left_sum >= cross_sum:
    return (left_low, left_high, left_sum)
  if right_sum >= left_sum and right_sum >= cross_sum:
    return (right_low, right_high, right_sum)
  if cross_sum >= left_sum and cross_sum >= right_sum:
      return (cross_low, cross_high, cross_sum)

left, right, sum = find_max_subarray(0, 15, array)
print(left)
print(right)
print(sum)