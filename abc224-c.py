n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

a = []
ans = 0
for i in range(n-1):
    for i_2 in range(n):
        for i_3 in range(n):
            if i < i_2 and i_2 < i_3:
                ans += 1
                a = (xy[i_2][1] - xy[i][1])*(xy[i_3][0] - xy[i_2][0]) - (xy[i_3][1] - xy[i_2][1])*(xy[i_2][0] - xy[i][0])
                if a == 0:
                    ans -= 1

print(ans)
