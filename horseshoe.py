shoes = input().split()
dic = {}
count = 0
for i in shoes:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for value in dic.values():
    count += value - 1
print(count)
