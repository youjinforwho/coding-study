board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i : i + 5] #보드 슬라이싱
        if tmp == tmp[::-1]: #역순으로 뒤집은 리스트와 비교
            cnt += 1
        for k in range(2):
            if board[i + k][j] != board[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1

print(cnt)