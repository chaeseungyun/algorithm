n = int(input())

res = []

for _ in range(n):
  x, y = map(int, input().split())
  res.append((x, y))

res.sort(key = lambda x: (x[1], x[0]))

for x, y in res:
  print(x, y)
