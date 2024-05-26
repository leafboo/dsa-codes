def isPalindrome(x):

  temporary_number = x
  compare_number = 0
  
  while temporary_number > 0:
    compare_number = (compare_number * 10) + (temporary_number % 10)
    temporary_number = temporary_number // 10

  if compare_number == x:
    return True
  return False

print(isPalindrome(323))
    