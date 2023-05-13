import heapq as hq #heappop, push 제공
a = [] #자료를 넣을 리스트
while True:
    n = int(input())
    if n == -1:  
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a)) #a에서 자료를 하나 꺼내서 return 
    else:
        hq.heappush(a, n) #a라는 리스트에 n값을 트리형태로 푸쉬
