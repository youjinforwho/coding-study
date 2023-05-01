num, m = map(int, input().split())
num = list(map(int, str(num))) #string 처리를 먼저 해줘야 인덱스로 접근할 수 있음
stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -=1
    stack.append(x)
if m != 0: #다 돌았는데도 빼야할 수가 남은 경우(스택에는 이미 내림차순대로 정렬되어있는 상태임)
    stack = stack[:-m] #남은 수만큼 뒤에서 빼주기
res = ''.join(map(str, stack)) #리스트의 요소들은 공백없이 붙이기
print(res)