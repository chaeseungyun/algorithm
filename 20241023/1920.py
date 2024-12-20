n = int(input())
a = list(map(int, input().split()))
target = set(a)
m = int(input())
b = list(map(int, input().split()))

for i in b:
  if i in target:
    print(1)
  else:
    print(0)