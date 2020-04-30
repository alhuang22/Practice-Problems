x  = int(input())
lis = []
for i in range(1, x + 1):
  lis.append(i)
if len(lis) % 2 == 1:
  print(-1)
else:
  i = 0
  while i < len(lis) - 1:
    temp = lis[i]
    lis[i] = lis[i+1]
    lis[i+1] = temp
    i += 2
  for i in lis:
    print(i, end=' ')
