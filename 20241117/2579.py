'''
d[i] == i번째의 가장 큰 계단합
전 계단을 밟고 도착, 전전 계단은 밟을 수 없음
s[n] + s[n-1] + d[n-3]

전전 계단을 밥고 도착
s[n] + d[n-2]
'''
n = int(input())
d = [0] * n
s = [int(input()) for _ in range(n)]
if len(s) <= 2:
  print(sum(s))
else:
  for i in range(2, n):
    d[0] = s[0] # 첫 번째 계단합
    d[1] = s[0] + s[1] # 두 번째 계단의 최대 계단합
    d[i] = max(s[i] + s[i-1] + d[i-3], s[i] + d[i-2]) # 점화식 사용
  print(d[-1])