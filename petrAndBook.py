pages = int(input())
reading = list(map(int,input().split()))
day = -1


while pages > 0:
    if day >= 6:
        day = -1
    day += 1
    pages -= reading[day]


print(day + 1)
