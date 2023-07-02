import sys
def DFS(L):
    global res
    if L == N:
        if max(money) - min(money) < res and len(set(money)) == 3: #세 사람의 총액이 서로 달라야 한다는 조건 추가
            res = max(money) - min(money)
    else: #가지가 세 갈래로 뻗어나가야 함
        for i in range(3):
            money[i] += li[L]
            DFS(L + 1)
            money[i] -= li[L] #뻗어나간 가지에서  다시 back 해줘야 함

if __name__ == "__main__":
    li = []
    N = int(input())
    money = [0] * 3
    for i in range(N):
        price = int(input())
        li.append(price)
    res = 2147000000
    DFS(0)
    print(res)