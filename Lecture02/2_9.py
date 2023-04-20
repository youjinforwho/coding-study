n = int(input())
res = []
for i in range(n):
    tmp = list(map(int, input().split())) #문자화된 숫자가 리스트로 들어감
    #a, b, c = map(int, tmp)
    tmp.sort(reverse = True)
    if tmp[0] == tmp[1] == tmp[2]: #가장 좋은 것을 먼저 조건으로 내걸어야 함
        prize = 10000 + tmp[0] * 1000
    elif tmp[0] == tmp[1] or tmp[1] == tmp[2] or tmp[0] == tmp[2]:
        prize = 1000 + tmp[0] * 100
    else:
        prize = tmp[0] * 100
    res.append(prize)
res.sort(reverse = True)
print(res[0])