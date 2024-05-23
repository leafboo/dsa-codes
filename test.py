def mergeSort(nums):
  if len(nums) > 1:
    left_arr = nums[:len(nums) // 2]
    right_arr = nums[len(nums) // 2:]

    # recursion
    mergeSort(left_arr)
    mergeSort(right_arr)

    i = 0
    j = 0
    k = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            nums[k] = left_arr[i]
            i += 1
        else:
            nums[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        nums[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        nums[k] = right_arr[j]
        j += 1
        k += 1 

arr = [-1,10,6,7,-7,1]
mergeSort(arr)
print(arr)
