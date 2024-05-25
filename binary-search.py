def findNumber(numbers, value):
  l = 0
  r = len(numbers) - 1

  while(l <= r):
    m = (l + r) // 2

    if numbers[m] < value:
      l = m + 1
    elif numbers[m] > value:
      r = m - 1
    else:
      return m
  return -1

numbers = [0, 2, 4, 6, 10]
print(findNumber(numbers, 1))