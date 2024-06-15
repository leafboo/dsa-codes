def climbStairs(n):
  one, two = 1, 1
  for i in range(n - 1):
    two += one
    one = two - one
  return two

print(climbStairs(3))