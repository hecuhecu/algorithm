x = input()
list = ['ch', 'o', 'k', 'u']
ans = "YES"
if x == '':
    ans = "YES"
else:
    ch = ''
    for i in x:
        if ch == 'c':
            if i == 'h':
                ch = ''
                continue
            else:
                ans = "NO"
                break
        elif i == 'c':
            ch = 'c'
        elif i in list:
            continue
        else:
            ans = "NO"
            break
print(ans)