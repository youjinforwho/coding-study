def DFS(L, sum, time):
    global res
    if time > m:
        return #가지치기로 끝내기
    if L == n: #부분집합이 완성 됐을 때
        if sum > res:
            res = sum
    else:
        DFS(L + 1, sum + pv[L], time + pt[L]) #문제 풀었을 때
        DFS(L + 1, sum, time) #문제 안풀 때

if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [0] * n
    pv = []
    pt = []
    solve = [[0] * 2 for _ in range(n)]
    print(solve)
    for i in range(n):
        x, y = map(int, input().split())
        pv.append(x)
        pt.append(y)
    DFS(0, 0, 0) #레벨, 총점, 시간
    print(res)