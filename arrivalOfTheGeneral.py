num = int(input())
line = list(map(int,input().split()))
big = line.index(max(line))
small = len(line)- 1 -line[::-1].index(min(line))
swaps = big + (len(line) - small) - 1
if small < big:
    swaps -= 1
print(swaps)
