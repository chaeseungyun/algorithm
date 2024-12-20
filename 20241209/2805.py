n, m = map(int, input().split())

trees = list(map(int, input().split()))

trees.sort()

def solve():
  start, end = 0, trees[n-1]
  result = 0
  
  while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in range(n):
      if mid < trees[i]:
        total += trees[i] - mid
  
    if total >= m:
      result = mid
      start = mid + 1

    else:
      end = mid - 1

  return result

print(solve())