
n = int(input())
count = 0
player = []
for i in range(n):
    height, weight = map(int, input().split())
    player.append((height, weight))
player.sort() #키 순대로 정렬
for i in range(n):
    num = 0
    for j in range(i + 1, n, 1):
        if (player[i][1] < player[j][1]):
            break
        else:
            num += 1
    if num == n - 1 - i:
        count += 1
print(count)