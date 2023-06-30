def DFS(L, sum):
    if L == K:
        if sum <= 0:
            return
        res.append(sum)
    else:
        DFS(L + 1, sum + chu[L])
        DFS(L + 1, sum - chu[L])
        DFS(L + 1, sum)
if __name__ == "__main__":
    K = int(input())
    chu = list(map(int, input().split()))
    res = []
    cnt = 0
    DFS(0, 0)
    ans = set(res)
    for i in range(1, sum(chu)):
        if i not in ans:
            cnt += 1
    print(cnt)