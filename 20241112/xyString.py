t = int(input())
def beforeX(s):
  return s[:-1]
def beforeY(s):
  return s[:-1][::-1]
res = []
for i in range(t):
  s = input().strip()
  e = input().strip()
  while len(e) > len(s):
    if not e: break
    if e[-1] == 'X':
       e = beforeX(e)
    elif e[-1] == 'Y':
      e = beforeY(e)
  if s == e: res.append('Yes')
  else: res.append('No')
for i, n in enumerate(res):
  print(f'#{i+1} {n}')