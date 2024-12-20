n = int(input())

def solve(k):
  if k == 1: return 1
  if k == 2: return 3
  if k == 3: return 5
  d = [0] * (k + 1)
  d[1] = 1
  d[2] = 3
  d[3] = 5
  for i in range(4, k + 1):
    d[i] += d[i-1] + d[i-2] * 2
  
  return d[k] % 10007

print(solve(n))