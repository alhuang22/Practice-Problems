num = int(input())
distances = list(map(int,input().split()))
closest = min(distances)
if distances.count(closest) > 1:
    print('Still Rozdil')
else:
    print(distances.index(closest) + 1)
