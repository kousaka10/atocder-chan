x, y = map(int, input().split('.'))

if 0 <= y and y <= 2:
    print(f'{x}-')
elif 3 <= y and y <= 6:
    print(f'{x}')
elif 7 <= y and y <= 9:
    print(f'{x}+')

