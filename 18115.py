from collections import deque
N = int(input())
skill = list(map(int, input().split()))
dq = deque()
for n in range(N - 1, -1, -1):
    if skill[n] == 1:
        dq.appendleft(N - n)
    elif skill[n] == 2:
        cur = dq.popleft()
        dq.appendleft(N - n)
        dq.appendleft(cur)
    else:
        dq.append(N - n)
print(*dq)
