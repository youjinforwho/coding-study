n = int(input())
a = list(map(int, input().split()))
avg = round(sum(a) / n) #round_half_even 방식 -> 4.5일때 홀수가 되므로 반올림이 안됨
min = a[0]
for idx, x in enumerate(a): #enumerate: idx와 value값을 쌍으로 대응시켜줌
    temp = abs(x - avg)
    if temp < min:
        min = temp
        score = x
        res = idx + 1
    elif temp == min:
        if x > score:
            score = x
            res = idx + 1
print(avg, res)