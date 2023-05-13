#str[A] = str1.get('A', 0) + 1 #딕셔너리에 A가 없으면 A에 0 할당
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1
for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]: #키 값이 다른 경우
            print("NO")
            break
    else:
        print("NO")
        break
else: #break에 걸린적이 없다면
    print("YES")