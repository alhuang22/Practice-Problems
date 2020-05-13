num = int(input())
arr = list(map(int,input().split()))
diff = 99999
for i in range(num):
    if i < num - 1:
        neighbors = abs(arr[i] - arr[i+1])
        if neighbors < diff:
            diff = neighbors
            val = (i+1,i+2)

if abs(arr[0] - arr[-1]) < diff:
    print(1, num)
else:
    for i in val:
        print(i,end=' ')
