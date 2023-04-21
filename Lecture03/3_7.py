n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
temp = sum = 0
diamond = n // 2
for i in range(n):
    for j in range(n):
        if (diamond - temp) <= j and (diamond + temp) >= j:
            sum += a[i][j]
    if i < diamond:
        temp += 1
    else:
        temp -= 1
print(sum)
