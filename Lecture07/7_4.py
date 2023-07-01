import sys
input = sys.stdin.readline
def DFS(L, price):
    global cnt
    if price > T: #가격이 넘어서버렸다면
        return #그대로 종료
    if L == k:
        if price == T: #금액이 맞춰졌다면
            cnt += 1 #가지수 1 증가시키기
    else:
        for i in range(N[L] + 1):
            DFS(L + 1, price + P[L] * i)

if __name__ == "__main__":
    T = int(input())
    k = int(input())
    P = []
    N = []
    cnt = 0
    total = 0
    for i in range(k):
        p, n = map(int, input().split())
        P.append(p)
        N.append(n)
    DFS(0, 0)
    print(cnt)