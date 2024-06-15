def find_seats(seats, students):
  seats.sort()
  students.sort()
  result = 0
  for i in range(len(seats)):
    if students[i] < seats[i]:
      result += seats[i] - students[i]
    elif students[i] > seats[i]:
      result += students[i] - seats[i]
    else:
      continue

  return result

seats = [3, 3, 1, 8, 5, 4, 8]
students = [2, 2, 7, 4, 8, 8, 4]
print(find_seats(seats, students))
# find the minimum number of moves to accomodate customers to available seats
