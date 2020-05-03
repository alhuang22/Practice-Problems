count = 0
num = int(input())
scores = list(map(int,input().split()))
worst = scores[0]
best = scores[0]
for i in range(1,num):
    if scores[i] > best:
        best = scores[i]
        count += 1
    if scores[i] < worst:
        worst = scores[i]
        count += 1
print(count)
