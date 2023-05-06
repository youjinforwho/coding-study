from collections import deque #덱을 쓰려면 꼭 호출해야 함
n, k = map(int, input().split())
dq = list(range(1, n + 1)) #1부터 n까지 리스트화
dq = deque(dq)
while dq:
    for _ in range(k - 1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()