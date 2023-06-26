#2차원 배열을 이용해서 그래프 구현
#1- 연결되어 있음, 0- 연결되어 있지 x
#항상 {행}에서 {열} 번호로 이동한다
import sys
n, m = map(int, input().split()) #n: 노드의 개수, m: 간선의 개수
g = [[0] * (n + 1) for _ in range(n + 1)] #1~n번 인덱스까지 만듦
for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(g[i][j], end = ' ')
    print() 