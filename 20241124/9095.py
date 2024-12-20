'''
4가 되는 방법은
1에서 4가 될 수 있고
2에서 4가 될 수 있고
3에서 4가 될 수 있다

점화식은
d[1] = 1
d[2] = 2
d[3] = 4
d[n] = d[n-1] + d[n-2] + d[n-3]( n > 3 )

d는? n번째 숫자를 구성하는 숫자의 합의 개수
'''

t = int(input())
n = [int(input()) for _ in range(t)]

m = max(n)

d = [0] * (m + 1)

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, m + 1):
  d[i] = d[i - 1] + d[i - 2] + d[i - 3]

for i in n:
  print(d[i])