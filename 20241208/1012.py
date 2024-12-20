import sys
sys.setrecursionlimit(10**6)

t = int(input())

for _ in range(t):
  n, m, k = map(int, sys.stdin.readline().split())
  
  graph = [[0] * m for _ in range(n)]

  for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1

  direction = [(1,0), (0,1), (-1,0), (0,-1)]
  visited = set()

  def dfs(x, y):
    visited.add((x, y))
    for dx, dy in direction:
      nx, ny = x + dx, y + dy
      if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 1 and (nx, ny) not in visited:
        dfs(nx, ny)

  count = 0
  for i in range(n):
    for j in range(m):
      if (i, j) not in visited and graph[i][j] == 1:
        dfs(i, j)
        count += 1
  
  print(count)