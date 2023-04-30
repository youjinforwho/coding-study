n = int(input())
seq = [0] * n
a = list(map(int, input().split()))
for i in range(n):
    cnt = j = 0
    while (cnt != a[i] or seq[j] != 0):
        if seq[j] == 0:
            cnt += 1
        j += 1
    seq[j] = i + 1

print(seq)