num = int(input())
count = 0
for i in range(num):
    op = str(input())
    if '+' in op:
        count += 1
    if '-' in op:
        count -= 1
print(count)
