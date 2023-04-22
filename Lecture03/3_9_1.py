dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a. insert(0, [0]*n)
a.append([0]*n)
for x in a: #앞뒤로 0 하나씩 넣어준다
    x.insert(0, 0)
    x.append(0)
cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)): #all() 안의 인자로 전달된 객체의 모든 요소가 참일 경우 True 반환, 그렇지 않은 경우는 False 반환
            cnt += 1
print(cnt)
        
