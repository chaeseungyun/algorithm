import sys

n = int(sys.stdin.readline())
arr = [0] * (10000 + 1)

for _ in range(n):
    i = int(sys.stdin.readline())
    arr[i] += 1

for i in range(10001):
    if arr[i] > 0:
        for _ in range(arr[i]):
            sys.stdout.write(str(i) + '\n')