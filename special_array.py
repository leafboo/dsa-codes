def specialArray(nums):
  
  def sort(arr):
    if len(arr) > 1:
      left_arr = arr[:len(arr) // 2]
      right_arr = arr[len(arr) // 2:]
     
      sort(left_arr)
      sort(right_arr)

      i = 0
      j = 0
      k = 0

      while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
          arr[k] = left_arr[i]
          i += 1
        else:
          arr[k] = right_arr[j]
          j += 1
        k += 1

      while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
      while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

  sort(nums)

  def binary_seach(arr, val):
    l = 0
    r = len(arr) - 1

    while l <= r:
      m = (l + r) // 2

      if arr[m] < val:
        l = m + 1
      elif arr[m] > val:
        r = m - 1
      else:
        return m
      
    return l


  for i in range(1, len(nums) + 1):
    if len(nums) - binary_seach(nums, i) == i:
      return i

  return -1



print(specialArray([0, 4, 3, 0, 4]))