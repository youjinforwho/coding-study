def DFS(L, k):
    if L == m:
        for i in range(L):
            print(li[i], end = ' ')
        print()
    else:
        for i in range(k, len(li)):
            li[L] = i
            DFS(L + 1, i + 1)
                
if __name__ == "__main__":
    n, m = map(int, input().split())
    li = [0] * (n + 1)
    DFS(0, 1)