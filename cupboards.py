num = int(input())
lCount = 0
rCount = 0
total = 0
for i in range(num):
    l,r = input().split()
    lCount += int(l)
    rCount += int(r)
status = False
if lCount + rCount == num and (lCount == num or rCount == num):
    print(0)
    status = True
if lCount > num // 2:
    total += num - lCount
else:
    total += lCount
if rCount > num // 2:
    total += num - rCount
else:
    total += rCount
if not status:
    print(total)
