#The testing on CodeForces either had a bug or python is too slow.
num = int(input())
arr = input().split()
qLength = input()
queries = input().split()
vasyaCount = 0
petyaCount = 0

for i in queries:
    num = arr.index(i)
    petyaNum = arr[::-1].index(i)
    vasyaCount += num + 1
    petyaCount += petyaNum + 1

print(vasyaCount, petyaCount)
