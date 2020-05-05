first = list(input())
second = list(input())
comb = first + second
comb.sort()

ground = list(input())
ground.sort()
if comb == ground:
    print('YES')
else:
    print('NO')
