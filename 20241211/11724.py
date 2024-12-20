import sys

n, m = map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10 ** 4)

graph = { i: [] for i in range(1, n + 1) }

for i in range(m):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)
  
visited = set()
def dfs(i):
  if i in visited:
    return
  visited.add(i)
  for k in graph[i]:
    if k not in visited:
      dfs(k)

count = 0
for i in range(1, n + 1):
  if i not in visited:
    dfs(i)
    count += 1

print(count)