n, k, l, c, d, p, nl, np = input().split()

totalML = int(k) * int(l)
mlToast = totalML // int(nl)

lime = (int(c) * int(d))
salt = int(p) // int(np)
toasts = min(mlToast, lime, salt) // int(n)

print(toasts)
