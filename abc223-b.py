S = input()

n = len(S)
i = 0
s = S
s_min = S
s_max = S
while i < n:
    s = s[1:n] + s[0]
    s_min = min(s, s_min)
    s_max = max(s, s_max)
    i += 1
print(s_min)
print(s_max)