p = list(map(int, input().split()))

alp = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    print(alp[p[i]-1], end='')

