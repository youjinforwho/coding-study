import itertools as it #수열, 조합을 알아서 구해주는 라이브러리
n, f = map(int, input().split())
b = [1] * n
cnt = 0
for i in range(1, n):
    b[i] = b[i - 1] * (n - i) / i
a = list(range(1, n + 1))
for tmp in it.permutations(a):
    sum = 0
    for L, x in enumerate(tmp):
        sum += (x*b[L])
    if sum == f:
        for x in tmp:
            print(x, end = ' ')
        break
