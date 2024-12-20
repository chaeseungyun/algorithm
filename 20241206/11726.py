n = int(input())

def solve(num):
  if num == 1: return 1
  if num == 2: return 2  
  d = [0] * (num + 1)
  d[1], d[2] = 1, 2
  for i in range(3, num + 1):
    d[i] += d[i - 1] + d[i - 2]
  return d[num] % 10007

print(solve(n))