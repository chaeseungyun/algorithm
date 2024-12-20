'''
f(0) = 1 0
f(1) = 0 1
f(2) = 1 1
f(3) = 1 2
f(4) = 2 3
f(5) = 3 5
f(6) = 5 8

f(n) = f(n-1) + f(n-2)
'''

t = int(input())
n = [int(input()) for _ in range(t)]

d = [[0, 0] for _ in range(41)]

d[0][0] = 1
d[1][1] = 1

m = max(n)

for i in range(2, m + 1):
  d[i][0] = d[i-1][0] + d[i-2][0]
  d[i][1] = d[i-1][1] + d[i-2][1]

for i in n:
  print(d[i][0], end= ' ')
  print(d[i][1])