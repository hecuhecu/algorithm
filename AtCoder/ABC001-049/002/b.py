w = input()
ans = ''
boin = ['a', 'i', 'u', 'e', 'o']
for i in w:
    if not i in boin:
        ans += i
print(ans)