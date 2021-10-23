H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]

flag = 1
for i in range(H-1):
    for j in range(W-1):
        for i_2 in range(H):
            for j_2 in range(W):
                if i < i_2 and j < j_2:
                    # print(i + 1, i_2 + 1, j + 1, j_2 + 1)
                    if not a[i][j] +a[i_2][j_2] <= a[i_2][j] + a[i][j_2]:
                        flag = -1

print("Yes" if flag == 1 else "No")

