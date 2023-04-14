#import sys
#sys.stdin=open("input.txt", "rt") 파일에서 값을 읽어옴
n, k = map(int, input().split()) #띄어쓰기를 구분해서 읽어옴

cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)