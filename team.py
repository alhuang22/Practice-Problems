num = int(input())
count = 0
for i in range(num):
    line = list(map(int,input().split()))
    if sum(line) >= 2:
        count += 1
print(count)
