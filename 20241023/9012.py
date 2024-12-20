t = int(input())
ps = []

for _ in range(t):
  ps.append(input())

def validVPS(ps):
  stack = []
  for s in ps:
    if s == '(':
      stack.append(s)
    else:
      if not stack:
        return 'NO'
      p = stack.pop()
      if p != '(':
        return 'NO'
  if stack:
      return 'NO'
  return 'YES'

for i in ps:
  print(validVPS(i))