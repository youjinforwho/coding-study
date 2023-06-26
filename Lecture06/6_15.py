import sys
def DFS(v):
    global cnt
    if v == n:
        cnt += 1
        for x in path:
            print(x, end = ' ')
        print()
    else:
        for i in range(1, n + 1): #n가지로 뻗는다
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop() #경로 출력
                ch[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    ch = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1 #방향 그래프
    cnt = 0
    path = []
    path.append(1)
    ch[1] = 1 #1번 노드부터 시작하므로
    DFS(1)
    print(cnt)