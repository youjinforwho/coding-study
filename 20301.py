from collections import deque
import sys
input = sys.stdin.readline
N, K, M = map(int, input().split())
Q = deque(list(range(1, N + 1)))
cnt = 0
flag = False
while Q:
    if flag == False:
        for i in range(K):
            Q.append(Q.popleft())
        print(Q.pop())
    else:
        for i in range(K):
            Q.appendleft(Q.pop())
        print(Q.popleft())
    cnt += 1
    if cnt == M:
        cnt = 0
        flag = not flag