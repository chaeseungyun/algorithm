n, m = map(int, input().split())
numbers = list(map(int, input().split()))
ranges = [list(map(int, input().split())) for _ in range(m)]

# 구간 합 구하기

# 각 숫자까지의 누적합 구하기

d = [0] * (n + 1)
d[0] = numbers[0] # 첫 번째 원소 할당

for i, v in enumerate(numbers):
  if i < 1: continue
  d[i] += d[i - 1] + v

res = []

for start, end in ranges:
  if start == 0: res.append(d[end - 1])
  res.append(d[end - 1] - d[start - 2])
