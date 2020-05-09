num, pos = list(map(int, input().split()))
#if pos > num//2 + 1 and num % 2 != 0:
    #index = pos
if num % 2 == 0 and pos <= num / 2:
    answer = pos * 2 - 1
elif num % 2 == 0 and pos > num / 2:
    answer = (pos - (num / 2)) * 2

if num % 2 != 0 and pos <= num // 2 + 1:
    answer = pos * 2 - 1
elif num % 2 != 0 and pos > num // 2 + 1:
    pos = pos - (num // 2 + 1)
    answer = pos * 2


print(int(answer))
