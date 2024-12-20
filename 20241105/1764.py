import sys
n, m = map(int, sys.stdin.readline().split())

tmp = set()
res = set()
for i in range(n):
  tmp.add(sys.stdin.readline())
for i in range(m):
  name = sys.stdin.readline()
  if name in tmp:
    res.add(name)
sys.stdout.write(str(len(res)) + '\n')
p = sorted(list(res))

for i in p:
  sys.stdout.write(i)