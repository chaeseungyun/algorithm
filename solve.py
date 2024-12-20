T = int(input())

def solve(k, arr):
  res = -9999999
  for i in range(0, len(arr)-k):
    a1 = sum(arr[i:i+k])
    for j in range(i+k, len(arr)-k + 1):
      a2 = sum(arr[j:j+k])
      res = max(res, a1 + a2)
  return res

res = []
for _ in range(T):
  n, k = map(int, input().split())
  arr = list(map(int, input().split()))
  res.append(solve(k, arr))
  
for i, n in enumerate(res):
  print(f'#{i+1} {n}')
  
  