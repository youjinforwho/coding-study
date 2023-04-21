max = 0 #-2147000000
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] #n줄을 읽어서 리스트화 시키겠다. 특별한 변수 지정 없을 때는 _(언더바) 사용
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if max < sum1:
        max = sum1
    if max < sum2:
        max = sum2
    
sum3 = 0
sum4 = 0
for i in range(n):
    sum3 += a[i][i]
    sum4 += a[n - i - 1][i]
if max < sum3:
    max = sum3
if max < sum4:
    max = sum4
print(max)
