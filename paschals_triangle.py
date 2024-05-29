def paschals_triangle(numRows):

  if numRows < 1 or numRows > 30:
    return "Invalid input"
  
  array = []

  for i in range(numRows):
    row = [0] * (i + 1)
    for j in range(i + 1):
      if j == 0 or j == i:
        row[j] = 1
      else:
        row[j] = array[i - 1][j - 1] + array[i - 1][j]
    array.append(row)

  return array

print(paschals_triangle(5))