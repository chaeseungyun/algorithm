n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

tCount = 0
pCount = (n // p, n % p)

for i in size:
  tCount += i // t + (1 if i % t != 0 else 0)

print(tCount)
print(f'{pCount[0]} {pCount[1]}')