a = input() #str1에 해싱
b = input() #str2에 해싱
str1 = [0] * 52
str2 = [0] * 52 #소문자 26개, 대문자 26개
for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1
    else:
        str1[ord(x) - 71] += 1 
for x in a:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str1[ord(x) - 71] += 1
for i in range(52):
    if str2[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")