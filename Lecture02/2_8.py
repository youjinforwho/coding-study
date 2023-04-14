def reverse(x):
    a = []
    res = 0
    for i in str(x):
        a.append(int(i)) #9, 3, 0이 담아진다
    a.reverse() #0, 3, 9가 담아진다
    for i in a:
        res *= 10
        res += i
    return res

def isPrime(x):
    temp = x - 1
    while (temp > 1):
        if (x % temp == 0):
            return (0)
        else:
            temp -= 1
    return (1)
n = int(input())
a = list(map(int, input().split()))
for i in a:
    if isPrime(reverse(i)) == 1:
        print(reverse(i), end = ' ')