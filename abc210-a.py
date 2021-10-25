n, a, x, y = map(int, input().split())

nedan = 0
if n > a:
    nedan = a*x+(n-a)*y
elif n <= a:
    nedan = n*x

print(nedan)