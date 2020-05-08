from math import sqrt
s1, s2, s3 = list(map(int,input().split()))

a = sqrt((s1 * s3) / s2)
b = sqrt((s1 * s2) / s3)
c = sqrt((s2 * s3) / s1)

print(int(4 * (a + b + c)))
