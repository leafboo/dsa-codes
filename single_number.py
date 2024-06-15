def single_number(nums):
  merge_sort(nums)
  unique_num = nums[0]
  for i in range(1, len(nums) - 1, 2):
    if nums[i] != nums[i + 1]:
      unique_num = nums[i + 1]
 
  return unique_num
  """
  alternative solution:
  unique_num = 0
  for num in nums:
    unique_nums = num ^ unique_nums
  return unique_nums
  """

def merge_sort(arr):
  if len(arr) > 1:
    left_arr = arr[:len(arr) // 2]
    right_arr = arr[len(arr) // 2:]

    merge_sort(left_arr)
    merge_sort(right_arr)

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

    while j < len(right_arr):
      arr[k] = right_arr[j]
      j += 1
      k += 1

    while i < len(left_arr):
      arr[k] = left_arr[i]
      i += 1
      k += 1


nums = [2, 2, 1]

print(single_number(nums))
