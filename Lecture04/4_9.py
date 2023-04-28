N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse = True)
cnt = 0
while a:
    if a[0] + a[-1] <= M:
        a.pop()
    a.pop(0)
    cnt += 1
print(cnt)