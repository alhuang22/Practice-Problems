num = str(input())

def magic():
    for i in range(len(num)):
        if (num[i] != '1') and (num[i] != '4'):
            print('NO')
            return
    if num[0] != '1':
        print('NO')
        return
    elif '444' in num:
        print('NO')
        return
    else:
        print('YES')
        return

magic()
