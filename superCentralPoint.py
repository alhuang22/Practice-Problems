num = int(input())
lis = []
count = 0
right = False
left = False
bottom = False
top = False

for i in range(num):
    x, y = list(map(int, input().split()))
    lis.append([x,y])

for i in lis:
    for j in lis:
        if j[0] > i[0] and j[1] == i[1]:
            right = True
        if j[0] < i[0] and j[1] == i[1]:
            left = True
        if j[1] < i[1] and i[0] == j[0]:
            bottom = True
        if j[1] > i[1] and i[0] == j[0]:
            top = True
    if right and left and bottom and top:
        count += 1
    right = False
    left = False
    bottom = False
    top = False
print(count)
