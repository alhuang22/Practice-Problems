num = int(input())
c1 = 0
c2 = 0
c3 = 0
for i in range(num):
	x = input().split()
	x = list(map(int, x))
	c1 += x[0]
	c2 += x[1]
	c3 += x[2]
if c1 == 0 and c2 == 0 and c3 == 0:
	print('YES')
else:
	print('NO')
