def digit_sum(x):
    sum = 0
    while (x > 0):
        sum = x % 10
        x //= 10
    return sum
n = int(input())
a = list(map(int, input().split()))
max = digit_sum(a[0])
for i in a:
    if max < digit_sum(i):
        max = digit_sum
        res = i
print(res)