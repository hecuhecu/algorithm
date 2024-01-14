a, b, c = map(int, input().split())
plus = False
minus = False
if a+b==c:
    plus = True
if a-b==c:
    minus = True
if plus and not minus:
    print("+")
elif not plus and minus:
    print("-")
elif plus and minus:
    print("?")
else:
    print("!")