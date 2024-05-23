def check_dup(nums, val):
  l = 0
  for r in range(1, len(nums)):
    if nums[r] != val:
      nums[l] = nums[r]
      l += 1

nums = [3, 2, 2, 3]
check_dup(nums, 3)

print(nums)