n = int(input())
nokori = 2025 - n
for i in range(1, 10):
    for j in range(1, 10):
        if i*j == nokori:
            print(i, "x", j)