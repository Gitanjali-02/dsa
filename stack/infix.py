def infix_to_postfix(expression):
    stack = []
    result = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for ch in expression:
        if ch.isalnum():
            result.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   priority.get(stack[-1], 0) >= priority[ch]):
                result.append(stack.pop())
            stack.append(ch)

    while stack:
        result.append(stack.pop())

    return ''.join(result)


exp = input("Enter infix expression: ")
print("Postfix:", infix_to_postfix(exp))