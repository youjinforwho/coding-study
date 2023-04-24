k, n = map(int, input().split())
len_max = 0
max = 0
a = []
for i in range(k):
    a.append(int(input()))
    max += a[i]
kijun = max // n
while (kijun != 0):
    b = 0
    for i in a:
        b += i // kijun
    if (b >= n):
        break
    kijun -= 1
print(kijun)