n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m): #회전 수행
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h - 1].append(a[h - 1].pop(0)) #h번째 행의 리스트가 하나 땡겨짐
    else:
        for _ in range(k):
            a[h - 1].insert(0, a[h - 1].pop())

sum = 0
temp = diamond = n // 2
for i in range(n):
    for j in range(n):
        if (diamond - temp) <= j and (diamond + temp) >= j:
            sum += a[i][j]
    if i < diamond:
        temp -= 1
    else:
        temp += 1
print(sum)