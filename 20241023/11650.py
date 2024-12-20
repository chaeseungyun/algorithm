import sys

n = int(sys.stdin.readline())
coord = []
for _ in range(n):
  coord.append(list(map(int, sys.stdin.readline().split())))
  
coord.sort(key=lambda x:(x[0], x[1]))

for i in coord:
  sys.stdout.write(str(i[0]) + ' ' + str(i[1]) + '\n')