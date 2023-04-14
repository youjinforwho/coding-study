n, m = map(int, input().split())
cnt = [0] * (m + n + 3)
for i in range(n):
    for j in range(m):
        cnt[i + j + 2] += 1
a = cnt[:]
a.sort(reverse = True)
for idx, x in enumerate(cnt):
    if x == a[0]:
        print(idx, end = ' ')