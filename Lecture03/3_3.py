card = list(range(21)) #0부터 20까지 자동으로 리스트화
for i in range(10):
    start, end = map(int, input().split())
    size = end - start + 1
    for j in range(size // 2):
        card[start + j], card[end - j] = card[end - j], card[start + j]
card.pop(0) #제일 앞에 있는거 하나 버려라
for i in card:
    print(i, end = ' ')