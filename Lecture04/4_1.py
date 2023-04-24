n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
pl = 0
pr = n - 1
mid = (pl + pr) // 2
while pl <= pr:
    if a[mid] == m:
        print(mid + 1)
    elif a[mid] > m:
        pr = mid - 1
    else:
        pl = mid + 1
    mid = (pl + pr) //2