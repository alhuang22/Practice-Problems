#Queue at the school
length, dur = input().split()
q = list(input())
length = int(length)
dur = int(dur)
count = 0
for i in range(dur):
  for j in range(length):
    if count >= length-1:
      break
    if j < length-1:
      if q[count + 1] == 'G' and q[count] == 'B':
        q[count] = 'G'
        q[count+1] = 'B'
        count += 2
      count += 1
  count = 0
print(''.join(q))

