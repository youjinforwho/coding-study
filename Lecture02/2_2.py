T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split()) #하나씩 split해서 mapping
    a = list(map(int, input().split()))
    a = a[s - 1 : e] #s번째 인덱스에 접근
    a.sort() #오름차순 정렬
    print("#%d %d" %(t + 1, a[k - 1])) #%에 대응한다는 뜻