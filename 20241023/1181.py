import sys

n = int(sys.stdin.readline())
seen = set()

for _ in range(n):
  seen.add(sys.stdin.readline())

result = sorted(list(seen), key=lambda x:(len(x), x))

for i in result:
  sys.stdout.write(i)