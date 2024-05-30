def find_judge(n, trust):
  # (outgoing)
  outgoing = {i: 0 for i in range(1, n + 1)}
  # (incoming)
  incoming = {i: 0 for i in range(1, n + 1)}

  for i in range(len(trust)):
    outgoing[trust[i][0]] += 1
    incoming[trust[i][1]] += 1
  
    


n = 3
trust = [[1, 3], [2, 3]]
print(find_judge(n, trust))