# 숫자를 나눌 수 있는 가장 큰 숫자의 개수의 합
# 다 나눠서 나머지가 0이 될 때 까지

n, k = map(int, input().split())
inputs = [int(input()) for _ in range(n)]

def solve(target):
  if target == 0:
    return target # 나눌 값이 없으면 바로 반환
  tmp = float('inf')
  newTarget = target
  for i in inputs:
    if i > target:
      break # 타겟보단 작거나 같은 숫자들 중
    if target // i < tmp:
      newTarget = target % i # 가장 큰 값으로 나눈 나머지
    tmp = min(target // i, tmp) # 타겟을 나눴을 때 가장 작은 몫을 가지는 값, 연산 횟수

  return tmp + solve(newTarget)

print(solve(k))
