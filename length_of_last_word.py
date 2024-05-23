def checkLength(s):
  counter = 0
  for i in reversed(range(len(s))):
    if s[i] != ' ':
      counter += 1

    if counter > 1 and s[i] == ' ':
      return counter

print(checkLength("   fly me   to   the moon  "))

