a = [list(map(int, input().split())) for _ in range(9)]
unique1 = True
for i in range(9):
    check1 = 0
    check2 = 0
    for j in range(9):
        check1 += a[i][j]
        check2 += a[j][i]
    if (check1 != 45 or check2 != 45): #행의 합 & 열의 합 중 하나라도 조건을 만족하지 못한경우
        unique = False

unique2 = True
for i in range(3): #그룹탐색
    for j in range(3):
        check3 = 0
        for k in range(3):
            for s in range(3):
                check3 += a[3 * i + k][3 * j + s] 
        if check3 != 45: #3x3짜리 사각형이 조건을 만족하지 못한 경우
            unique = False
    
if unique1 and unique2:
    print("YES")
else:
    print("NO")