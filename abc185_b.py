n, m, t = map(int, input().split())
ab = []
## 開始時の時間
ab.append([0, 0])
i = 1
while i <= m:
    a, b = map(int, input().split())
    ab.append([a, b])
    i += 1
## 終了時の時間
ab.append([t, t])
# print(ab)

M = len(ab)
num = n
for i in range(M-1):
    ## 移動ロス
    num += ab[i][1] - ab[i + 1][0]
    # print(i, "移動", num)
    ## バッテリー切れならば
    if num <= 0:
        break
    ## 充電
    num += ab[i+1][1] - ab[i+1][0]
    # print(i, "充電", num)
    ## バッテリーオーバーするとき
    if num > n:
        ## バッテリーを満タンにリセット
        num = n
    # print(i, "充電補正後", num)

print("Yes" if num > 0 else "No")
# print(num)

