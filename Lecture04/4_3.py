n, m = map(int, input().split())
#가능한 용량의 수 중 이분탐색으로 최소 용량 찾기
def Count(capacity):
    cnt = 1
    sum, count = 0, 1
    for x in DVD:
        if sum + x <= capacity:
            a += x
        else:
            a = x
            count += 1
    return count

DVD = list(map(int, input().split()))
pl = 1
pr = sum(DVD)
min = sum(DVD)
while pl <= pr:
    mid = (pl + pr) // 2
    count = Count(mid)
    if count <= m:
        pr = mid - 1
        min = mid
    else:
        pl = mid + 1
print(min)
