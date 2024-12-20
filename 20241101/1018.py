wBoard= [['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W']]

bBoard = [['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B'],
         ['B','W','B','W','B','W','B','W'],
         ['W','B','W','B','W','B','W','B']]

n, m = map(int, input().split()) # n: 행, m: 열
board = [input() for _ in range(n)]

def comparisonBoard(x, y):
  bCount = 0
  wCount = 0
  for i in range(x, x+8): # 열
    for j in range(y, y+8): # 행
        if board[j][i] != wBoard[j-y][i-x]:
          wCount += 1
        if board[j][i] != bBoard[j-y][i-x]:
          bCount += 1
  return min(bCount, wCount)

res = 64

for x in range(m-7): # 열
  for y in range(n-7): # 행
    res = min(res, comparisonBoard(x,y))

print(res)