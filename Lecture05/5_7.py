from collections import deque
curry = input()
case = int(input())
for i in range(case):
    plan = input()
    dq = deque(curry)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i + 1))
                break
    else:
        if len(dq) == 0:
            print("#d YES" %(i + 1))
        else:
            print("#%d NO" %(i + 1))