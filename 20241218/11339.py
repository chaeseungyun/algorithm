n = int(input())

nums = sorted(list(map(int, input().split())))

d = [0] * n
d[0] = nums[0]
for i in range(1, n):
  d[i] += d[i - 1] + nums[i]

print(sum(d))