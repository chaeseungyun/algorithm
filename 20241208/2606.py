computer = int(input())
pair = int(input())
graph = {i: [] for i in range(1, computer + 1)}
for _ in range(pair):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visited = set()
def dfs(i):
  visited.add(i)
  for j in graph[i]:
    if j not in visited:
      dfs(j)
dfs(1)
print(len(visited) - 1)