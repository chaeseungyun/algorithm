from collections import deque
n, m, v = map(int, input().split())
nodes = [tuple(map(int, input().split())) for _ in range(m)]
  
def DFS():
  stack = []
  res = []
  stack.append(v)

  while stack:
    p = stack.pop()
    if p in res:
      continue # 이미 지나간 길이면 패스
    cur = []
    for node in nodes:
      if p in node:
        a, b = node
        target = a if a != p else b
        if not target in res:
          cur.append(target) # 이미 지나간 길이면 패스
    stack.extend(sorted(cur, reverse=True))
    res.append(p)
    
  for i in res:
      print(i, end=' ')

DFS()
print()

def BFS():
  queue = deque()
  res = []
  queue.append(v)
  
  while queue:
    q = queue.popleft()
    if q in res:
      continue
    cur = []
    for node in nodes:
      if q in node:
        a, b = node
        target = a if a != q else b
        if not target in res:
          cur.append(target)
    queue.extend(sorted(cur))
    res.append(q)
  for i in res:
      print(i, end=' ')
BFS()