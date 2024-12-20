T = int(input())
res = []

def checkSame(arr):
  for i in arr:
    if i != arr[0]: return False
  return True

def checkSameRotate(k, arr):
  seen = set()
  target = arr
  c = 0
  
  while not checkSame(target):
    tmp = target[k-1]
    target.append(tmp)
    target = target[1:]
    if tuple(target) in seen: return -1
    seen.add(tuple(target))
    c += 1
    
  return c

for _ in range(T):
  n, k = map(int, input().split())
  arr = list(map(int, input().split()))
  res.append(checkSameRotate(k, arr))

for i, n in enumerate(res):
  print(f'#{i+1} {n}')