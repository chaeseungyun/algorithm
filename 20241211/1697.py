import sys
sys.setrecursionlimit(10 ** 6)
n, k = map(int, input().split())

def dfs(i, count):
  if i == k:
    return count
  if i - 1 >= 0:
    return min(dfs(i-1, count + 1), dfs(i + 1, count + 1), dfs(i * 2, count + 1))
  return min(dfs(i + 1, count + 1), dfs(i * 2, count + 1))

print(dfs(n, 0))
