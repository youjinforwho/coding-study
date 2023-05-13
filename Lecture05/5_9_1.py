#str[A] = str1.get('A', 0) + 1 #딕셔너리에 A가 없으면 A에 0 할당
a = input()
b = input()
sH = dict()

for x in a:
    sH[x] = sH.get(x, 0) + 1
for x in b:
    sH[x] = sH.get(x, 0) - 1
for x in a:
    if sH.get(x) > 0:
        print("NO")
        break
else:
    print("YES")