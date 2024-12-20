n = int(input())
count = 0
while n > 1:
  if n % 3 == 0:
    n /= 3
  elif (n - 1) % 3 == 0:
    n -= 1
  elif n % 2 == 0:
    n /= 2
  elif (n - 1) % 2 == 0:
    n -=1
  else:
    n -= 1
  count +=1
  
print(count)

# dp 문제