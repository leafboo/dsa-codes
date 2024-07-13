def distance_to_char(s, c):

  temp = []
  for i in range(1, len(s)):
    if s[i] == c:
      temp.append(i)
  return temp

s = "loveleetcode"
c = "e"
print(distance_to_char(s, c))

# create a new array
# loop over the string and replace the c characters in the string to 0
