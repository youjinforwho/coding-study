N = int(input())
a = list(map(int, input().split()))
b = []
while a:
    if a[0] > a[-1]:
        b.append(a[-1])
        a.pop()
    else:
        b.append(a[0])
        a.pop(0)
    if b[-1] >= a[0] and b[-1] >= a[-1]:
        break
print(b)
        