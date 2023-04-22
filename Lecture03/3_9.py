n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
bonguri = 0
for i in range(n):
    for j in range(n):
        if i > 0 and a[i - 1][j] > a[i][j]:
            pass
        elif i + 1 < n and a[i + 1][j] > a[i][j]:
            pass
        elif j > 0 and a[i][j - 1] > a[i][j]:
            pass
        elif j + 1 < n and a[i][j + 1] > a[i][j]:
            pass
        else:
            bonguri += 1
print(bonguri)