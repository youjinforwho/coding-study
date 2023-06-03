import sys
def DFS(sum, cnt):
    global res
    if cnt > res:
        return 
    if sum > m:
        return
    elif sum == m:
        if cnt < res:
            res = cnt #새롭게 정의하는 부분이 있어서 지역변수가 되버림 -> global 써야 함
    else:
        for i in coin:
            DFS(sum + i, cnt + 1)

if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    coin.sort(reverse = True)
    res = int(2e9)
    DFS(0, 0)
    print(res)