from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
Q = deque((pos, val) for pos, val in enumerate(list(map(int, input().split()))))
cur = Q.popleft()
res = [cur[0] + 1]
while Q:
    if cur[1] > 0:
        for i in range(cur[1]):
            Q.append(Q.popleft())
        cur = Q.pop()
        res.append(cur[0] + 1)
    else:
        for i in range((-1)*cur[1]):
            Q.appendleft(Q.pop())
        cur = Q.popleft()
        res.append(cur[0] + 1)
print(' '.join(map(str, res)))
    