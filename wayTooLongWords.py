num = int(input())
sol = []
for i in range(num):
    word = input()
    if len(word) > 10:
        first = word[0]
        last = word[-1]
        secLast = len(word)-1
        mid = len(word[1:secLast])
        abb = first + str(mid) + last
        sol.append(abb)
    else:
        sol.append(word)

for i in sol:
    print(sol)
