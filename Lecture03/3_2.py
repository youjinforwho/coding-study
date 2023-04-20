def isYaksu(x):
    cnt = 0
    temp = x
    while temp != 0:
        if x % temp == 0:
            cnt += 1
        temp -= 1
    return cnt


s = input()
res = 0
for i in s:
    if i.isdecimal(): #0~9의 숫자면 True 반환
        res = res * 10 + int(i)
print(res)
print(isYaksu(res))