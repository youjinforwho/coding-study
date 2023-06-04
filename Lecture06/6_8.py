def DFS(L):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1 #체크 켰다
                res[L] = i
                DFS(L + 1) 
                ch[i] = 0 #체크 풀었다

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    ch = [0] * (n + 1)
    cnt = 0
    DFS(0)
    print(cnt)