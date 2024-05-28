def paschals_triangle(numRows):

  if numRows < 1 or numRows > 30:
    return "Invalid input"
  
  array = []

  for i in range(numRows):
    row = [0] * (i + 1)
    for j in range(i + 1):
      row[j] = j
    array.append(row)

  return array

print(paschals_triangle(4))