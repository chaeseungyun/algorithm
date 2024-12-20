n = int(input())
target = input().split()
m = int(input())
cards = input().split()

seen = {}
for card in target:
  if seen.get(card):
    seen[card] += 1
  else:
    seen[card] = 1

res = [str(seen.get(x, 0)) for x in cards]
print(' '.join(res))
