count = 0
n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    sum = a[i]
    j = i + 1
    if (sum == m):
        count += 1
    while (sum < m and j < n):
        sum += a[j]
        j += 1
        if (sum == m):
            count += 1
print(count)