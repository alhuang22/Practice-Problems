capacity = 0
maxCapacity = 0
num = int(input())
for i in range(num):
    line = input().split()
    exit = int(line[0])
    enter = int(line[1])
    capacity -= exit
    capacity += enter
    if capacity > maxCapacity:
        maxCapacity = capacity
print(maxCapacity)
