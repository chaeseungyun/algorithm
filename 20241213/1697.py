from collections import deque

n, k = map(int, input().split())

queue = deque()

visited = set()

def bfs(i):
  queue = deque()
  queue.append((i, 0))
  visited.add(i)

  while queue:
    current, count = queue.popleft()
    
    if current == k:
      return count

    for d in [current - 1, current + 1, current * 2]:
      if d not in visited and (d < 100001 and d >= 0):
        queue.append((d, count + 1))
        visited.add(d)

print(bfs(n))