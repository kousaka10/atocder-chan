s = list(input())
t = list(input())

if s == t:
    print("Yes")
    exit()
n = len(s)
for i in range(n-1):
    s[i], s[i+1] = s[i+1], s[i]
    if s == t:
        print("Yes")
        exit()
    s[i], s[i + 1] = s[i + 1], s[i]
print("No")

# s = input()
# t = input()
# if(s==t): exit(print('Yes'))
# for i in range(len(s)-1):
#     if s[:i] + s[i+1] + s[i] + s[i+2:] == t:
#         exit(print('Yes'))
# print("No")