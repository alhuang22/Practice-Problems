import math
prime = True
printed = False
x = input().split()
x = list(map(int,x))
for i in range(x[0] + 1, x[1]+1):
  sq = int(math.sqrt(i))
  for j in range(2,sq + 1):
    if i % j == 0:
      prime = False
      break
  if prime and i != x[1]:
    print('NO')
    printed = True
    break
  if prime and i == x[1]:
    print('YES')
    printed = True
  prime = True
if not printed:
  print('NO')
