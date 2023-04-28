#그리디: 현재 단계에서 가장 좋은 것만을 가져감 
#대부분이 정렬 먼저->차례차례 선택해가는 방식으로 해결이 됨
#회의가 끝나는 시간 기준으로 정렬하기
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split)
    meeting.append((s, e)) #튜플 형태로 끝~시작시간 저장
meeting.sort(key = lambda x : (x[1], x[0])) #끝나는 시간 기준으로 정렬하기
end_time = 0
cnt = 0
for s, e in meeting:
    if s >= end_time:
        end_time = e
        cnt += 1
print(cnt)
    
