n, k = map(int, input().split())

def fac(n):
  res = 1
  for i in range(1, n+1):
    res *= i
  return res

print(int(fac(n) / fac(n-k) / fac(k)))