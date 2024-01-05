n, k = map(int, input().split())
s = input()

ans = list(s)

for i in range(n):
    l = i
    for j in range(i+1, n):
        # 現在の i 番目の文字より小さい文字があるか探す
        if ans[l] > ans[j]:
            # あった
            ss = ans.copy()
            ss[i], ss[j] = ss[j], ss[i]
            # ss と比較したとき、違う数
            diff = 0
            for t in range(n):
                if ss[t] != s[t]:
                        diff += 1
            if diff <= k:
                l = j
            # lを更新。次はl番目より小さい文字を探す
    ans[i], ans[l] = ans[l], ans[i]

print("".join(ans))