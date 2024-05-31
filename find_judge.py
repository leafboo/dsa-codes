def find_judge(n, trust):
  # (outgoing)
  outgoing = {i: 0 for i in range(1, n + 1)}
  # (incoming)
  incoming = {i: 0 for i in range(1, n + 1)}

  for i in range(len(trust)):
    outgoing[trust[i][0]] += 1
    incoming[trust[i][1]] += 1
  
  for key in incoming.keys():
    if outgoing[key] == 0 and incoming[key] == n - 1:
      return key
  return -1


n = 3
trust = [[1, 2], [2, 3]]
print(find_judge(n, trust))