num = int(input())
fingers = list(map(int,input().split()))
ans = 0
options = [1, 2, 3, 4, 5]
back = num + 1
count = sum(fingers) - 1

for i in options:
    if (count + i) % back != 0:
        ans += 1
print(ans)
