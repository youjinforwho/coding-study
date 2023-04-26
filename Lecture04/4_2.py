#결정 알고리즘의 특징 : 특정 범위 안에 있다는 것을 알 수 있음. 범위 내의 이분탐색
#k, n = map(int, input().split()) 
#len_max = 0
#max = 0
#a = []
#for i in range(k):
#    a.append(int(input()))
#    max += a[i]
#kijun = max // n
#while (kijun != 0):
#    b = 0
#    for i in a:
#        b += i // kijun
#    if (b >= n):
##        break
 #   kijun -= 1
#print(kijun)

k, n = map(int, input().split())
a = []
for i in range(k):
    a.append(int(input()))
a.sort(reverse = True)
pl = 1
pr = a[0]
max = -2147000000
while (pl <= pr):
    b = 0
    mid = (pl + pr) // 2
    for i in a:
        b = i // mid
    if b < n:
        pr = mid - 1
    else:
        if (max < mid):
            max = mid
        pl = mid + 1
print(max)