from math import ceil

length, m = list(map(int, input().split()))
line = list(map(int, input().split()))
ans = 0
p = 0

for i in range(length):
    x = ceil(line[i] / m)
    if x >= ans:
        ans = x
        p = i + 1
print(p)
