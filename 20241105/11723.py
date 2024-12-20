import sys
m = int(sys.stdin.readline())
tmp = set([str(i) for i in range(1, 21)])
s = set()
for _ in range(m):
  i = sys.stdin.readline().split()
  if i[0] == 'add':
    s.add(i[1])
  elif i[0] == 'remove':
    if i[1] in s:
      s.remove(i[1])
  elif i[0] == 'check':
    print(1 if i[1] in s else 0)
  elif i[0] == 'toggle':
    if i[1] in s:
      s.remove(i[1])
    else: s.add(i[1])
  elif i[0] == 'all':
    s.clear()
    s = tmp.copy()
  elif i[0] == 'empty':
    s.clear()