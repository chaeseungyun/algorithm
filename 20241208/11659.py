import sys
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, input().split()))
period = []
for _ in range(m):
  period.append(tuple(map(int, sys.stdin.readline().split())))
d = [0] * (n + 1)
for i in range(1, n+1):
  d[i] += d[i - 1] + nums[i - 1]
for s, e in period:
  sys.stdout.write(str(d[e] - d[s-1]) + '\n')