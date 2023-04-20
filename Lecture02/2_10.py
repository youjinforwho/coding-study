n = int(input())
bonus = 1
score = 0
problem = list(map(int, input().split()))
for i in range(n):
    if problem[i] == 1:
        score += bonus
        bonus += 1
    else:
        bonus = 1
print(score)
