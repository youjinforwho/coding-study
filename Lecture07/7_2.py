import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def DFS(L, sum): #레벨, 금액, 날짜
    global res
    if L > n:
        return
    elif L == n:
        if sum > res:
            res = sum
    else:
        DFS(L + T[L], sum + P[L])#상담 받았을 때
        DFS(L + 1, sum)#상담 안받았을 때

if __name__ == "__main__":
    n = int(input())
    T = []
    P = []
    ch = [0] * n
    for i in range(n):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)
    res = 0
    DFS(0, 0)
    print(res)