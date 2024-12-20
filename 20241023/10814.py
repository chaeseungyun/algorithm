import sys

n = int(sys.stdin.readline())
res = []
for _ in range(n):
  res.append(sys.stdin.readline().split())

res.sort(key=lambda x:int(x[0]))

for i in res:
  sys.stdout.write(str(i[0] + ' ' + i[1] + '\n'))