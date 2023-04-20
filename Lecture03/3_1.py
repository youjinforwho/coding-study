n = int(input())
for i in range(n):
    huimoon = True
    k = input()
    k.upper()
    for j in range(len(k)//2): #정수 결과를 얻고 싶다면 / 연산자를 두 개 쓴다
        if (k[j] != k[-(j + 1)]):
            huimoon = False
    if huimoon:
        print("#%d YES" %(i + 1))
    else:
        print("#%d NO" %(i + 1))