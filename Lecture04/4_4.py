def Count(min_distance):
    temp = magugan[0]
    count = 1
    for x in range(1, n, 1):
        distance = magugan[x] - temp
        if (distance >= min_distance):
            count += 1
            temp = magugan[x]
    return (count)


n, c = map(int, input().split())
magugan = []
for i in range(n):
    magugan.append(int(input()))
magugan.sort()
res = pl = 1
pr = magugan[n - 1] - magugan[0]

while (pl <= pr):
    mid = (pl + pr) // 2
    count = Count(mid)
    if count >= c:
        pl = mid + 1
        if (res < mid):
            res = mid
    else:
        pr = mid - 1
print(res)