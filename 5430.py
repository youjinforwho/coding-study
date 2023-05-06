import sys
from collections import deque
input = sys.stdin.readline

def print_res(li):
    print('[' +','.join(map(str, li)) + ']')

case = int(input())
for i in range(case):
    error = False
    order = input()
    ord = [0] * 400001
    ord[0] = order[0]
    k = 0
    for i in range(len(order) - 1):
        if order[i] == order[i + 1]:
            ord[k] += order[i + 1]
        else:
            k += 1
            ord[k] = order[i + 1]
    n = int(input())
    arr = input().rstrip().strip("[""]").split(",")
    li = []
    for i in range(n):
        li.append(int(arr[i]))
    li = deque(li)
    for i in range(k):
        if ord[i][0] == 'R':
            if len(ord[i]) % 2 != 0:
                li.reverse()
        elif ord[i][0] == 'D':
            for i in range(len(ord[i])):
                if li:
                    li.popleft()
                else:
                    print("error")
                    error = True
                    break
    if error == False:
        print_res(li)
