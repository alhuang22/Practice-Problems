first = str(input())
second = str(input())
ans = []
for i in range(len(first)):
  if first[i] != second[i]:
    ans.append('1')
  else:
    ans.append('0')

print(''.join(ans))
