n = int(input())
i = 0
a = []
b = []
while i < n:
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)
    i += 1

t = 0
for i in range(n):
    t = t + a[i] / b[i]

t_c = t / 2
t = 0
ans = 0
d = 0
for i in range(n):
    t = t + a[i] / b[i]
    d = d + a[i]
    if t > t_c:
        ans = d + b[i] * (t_c - t)
        break

print(ans)