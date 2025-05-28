# 짝지어 제거하기, 12973
# 문자열의 길이 <= 1_000_000

def solution(s):
    stack = []
    for v in s:
        if stack and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
    return int(not stack)

solution('baabaa')