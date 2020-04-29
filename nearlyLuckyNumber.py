num = str(input())
luck = 0
for i in num:
  if i == '4' or i == '7':
    luck += 1
if luck == 4 or luck == 7:
  print('YES')
else:
  print('NO')