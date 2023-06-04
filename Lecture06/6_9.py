import sys
def DFS(L):
    global res
    if L == n:
        for i in range(len(p)):
            res += b[i] * p[i]
        if res == f:
            print(*p)
            sys.exit(0)
        res = 0
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i + 1
                DFS(L + 1)
                ch[i] = 0
        

if __name__ == "__main__":
    res = 0
    n, f = map(int, input().split())
    p = [0] * n #순열 저장
    b = [1] * n #이항 계수 저장 -> 이항계수의 처음/끝은 항상 1이므로
    ch = [0] * n #중복 방지를 위한 체크 배열
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i #조합 구하기
    DFS(0)

