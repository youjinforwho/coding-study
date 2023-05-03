exp = input()
stack = []
for i in exp:
    if i == '*':
        stack[-2] = stack[-2] * stack[-1]
        stack.pop()
    elif i == '/':
        stack[-2] = stack[-2] // stack[-1]
        stack.pop()
    elif i == '+':
        stack[-2] = stack[-2] + stack[-1]
        stack.pop()
    elif i == '-':
        stack[-2] = stack[-2] - stack[-1]
        stack.pop()
    else:
        stack.append(int(i))
print(stack[-1])