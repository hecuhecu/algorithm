# a = int(input())
# b = int(input())
# ac = a
# bc = b
# ans1 = 0
# while ac != bc:
#     if ac == 9:
#         ac = 0
#     else:
#         ac += 1
#     ans1 += 1

# ans2 = 0
# while a != b:
#     if a == 0:
#         a = 9
#     else:
#         a -= 1
#     ans2 += 1
# print(min(ans1, ans2))

a = int(input())
b = int(input())
print(min(abs(a-b), 10-abs(a-b)))