s = input()
t = input()
list = ['a', 't', 'c', 'o', 'd', 'e', 'r']
ans = 'You can win'
for i in range(len(s)):
  if s[i] == t[i]:
    continue
  elif s[i] == '@' and t[i] in list:
    continue
  elif t[i] == '@' and s[i] in list:
    continue
  else:
    ans = 'You will lose'
    break
print(ans)