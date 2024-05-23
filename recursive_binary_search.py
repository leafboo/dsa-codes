def recursive_binary_seach(list, target):
  if len(list) == 0: # base case
    return False
  else:
    midpoint = (len(list)) // 2

  if list[midpoint] == target: # base case
    return True
  else:
    if list[midpoint] < target:
      return recursive_binary_seach(list[slice(midpoint + 1, len(list))], target)
    else:
      return recursive_binary_seach(list[slice(0, midpoint)], target)
    
print(recursive_binary_seach([1, 2, 3, 4, 5, 6, 7, 8] , 5))