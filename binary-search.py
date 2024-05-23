numbers = [-1, 0, 3, 5, 9, 12]

def findNum(input):
  left = 0
  right = len(numbers) - 1

  while left <= right:
    mid = (left + right) // 2

    if numbers[mid] > input:
      right = mid - 1
    elif numbers[mid] < input:
      left = mid + 1  
    else:
      return mid
  return -1

print(findNum(-2))