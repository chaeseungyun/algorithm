n, r, c = map(int, input().split())

d = [[0] * 2 ** n for j in range(2**n)]

count = 0
def solve(length, s, e, c):
  if length == 2:
    1