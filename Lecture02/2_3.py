n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set() #중복제거함수
for i in range(n): #첫번째 수 뽑기
    for j in range(i + 1, n): #두번째 수 뽑기
        for m in range(j + 1, n): #세번째 수 뽑기
            res.add(a[i] + a[j] + a[m])
            print(a[i] + a[j] + a[m])
res = list(res) #res를 list화 시켜줌
res.sort(reverse = True) #내림차순으로 정렬하기
print(res[k - 1])