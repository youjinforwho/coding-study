exp = input() #+나 -를 만나면 스택에 있는 내용을 전부 꺼내준다
#*/를 만나면 *와 /만 꺼내줌
#여는 괄호와 닫는 괄호 사이에 있는 연산자 모두 처리
stack = []
res = ''
for x in exp:
    if x== '(':
        stack.append(x)
    elif x == '*' or x == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            res += stack.pop()
        stack.append(x)
    elif x == '+' or x == '-':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(x)
    elif x == ')':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.pop()
    else:
        res += x
while stack: #남아있는 연산자 처리
    res += stack.pop()
print(res)
