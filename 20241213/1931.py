# greedy!

n = int(input())

meetings = [list(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1], x[0]))

lastEnd = 0
count = 0
for start, end in meetings:
  
  if start >= lastEnd:
    lastEnd = end
    count += 1

print(count)