import sys

n = int(input())

coord = list(map(int, sys.stdin.readline().split()))

distinct = sorted(list(set(coord)))

order = dict()

for v, i in enumerate(distinct):
  order[i] = v

for i in range(len(coord)):
  print(order[coord[i]], end=' ' if i < n - 1 else '')
