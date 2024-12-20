from collections import deque
t = int(input())
res = []
for _ in range(t):
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  ordered = [(a[i], i) for i in range(len(a))]
  v = ordered[m][0]
  o = ordered[m][1]
  q = deque(ordered)
  i = 0
  while q:
    popped = q.popleft()
    if len([x for x in q if popped[0] < x[0]]):
      q.append(popped)
    else:
      i += 1
      if (popped[0] == v and popped[1] == o):
        res.append(i)
        break
for i in res:
  print(i)