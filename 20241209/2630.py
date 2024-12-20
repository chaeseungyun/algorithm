import sys

n = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

blue, white = 0, 0
def solve(rs, re, cs, ce):
  b, w = 0, 0
  
  for i in range(cs, ce):
    for j in range(rs, re):
      if paper[i][j] == 0:
        w += 1
      else:
        b += 1
  if b == 0:
    global white
    white += 1
    return
  if w == 0:
    global blue
    blue += 1
    return
  
  midRow = (re + rs) // 2
  midCol = (ce + cs) // 2

  # 왼쪽 위
  solve(rs, midRow, cs, midCol)
  # 오른쪽 위
  solve(midRow, re, cs, midCol)
  # 왼쪽 아래
  solve(rs, midRow, midCol, ce)
  # 오른쪽 아래
  solve(midRow, re, midCol, ce)
    
solve(0, len(paper), 0, len(paper))

print(white)
print(blue)