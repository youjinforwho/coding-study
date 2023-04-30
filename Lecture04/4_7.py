L = int(input())
box = list(map(int, input().split()))
n = int(input())
for i in range(n):
    box.sort()
    box[0] += 1
    box[-1] -= 1
box.sort()
print(box[-1] - box[0])