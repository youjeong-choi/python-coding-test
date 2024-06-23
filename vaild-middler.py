def solution(s):
    stack = [];
    for c in s:
        if c == '(': # 괄호가 '('인 경우
            stack.append(c)
        else: # 괄호가 ')'인 경우
            if not stack: # 스택이 비어있다면 무조건 False
                return False
            elif stack[-1] == '(': # 스택의 마지막 원소가 '('인 경우
                stack.pop()

            # else: # 스택의 마지막 원소가 '('인 경우 밖에 없기 때문
            #     stack.pop()

    return not stack