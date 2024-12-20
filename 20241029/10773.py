import sys
from collections import deque
numbers = deque()
n = int(sys.stdin.readline())
sum = 0
for _ in range(n):
  k = int(sys.stdin.readline())
  if k == 0:
    sum -= numbers.pop()
  else:
    numbers.append(k)
    sum += k
print(sum)