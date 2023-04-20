n = int(input())
k = list(map(int, input().split()))
l = int(input())
s = list(map(int, input().split()))
a = k + s
a.sort()
for i in a:
    print(i, end = ' ')