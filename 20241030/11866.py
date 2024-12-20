import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
p = deque([str(x+1) for x in range(n)])
res = []
start = k - 1
while p:
  p.rotate(-start)
  res.append(p.popleft())
sys.stdout.writelines('<' + ', '.join(res) + '>')