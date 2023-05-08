from collections import deque
import sys
input = sys.stdin.readline
case = int(input())
for i in range(case):
    n = int(input())
    Q = deque(list(map(str, input().split())))
    res = [Q.popleft()]
    while Q:
        if ord(res[0]) < ord(Q[0]):
            res.append(Q.popleft())
        else:
            res.insert(0, Q.popleft())
    print(''.join(map(str, res)))
