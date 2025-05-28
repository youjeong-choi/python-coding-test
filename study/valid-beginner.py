class Solution:
    def __init__(self):
        self.bracket_pairs = {'(': ')', '{': '}', '[': ']'}
        self.open_brackets = set(self.bracket_pairs.keys())

    def isValid(self, s: str):
        stack = []

        for c in s:
            if c in self.open_brackets: # 열린 괄호인 경우
                stack.append(c)
            else: # 닫힌 괄호인 경우
                if not stack: # 스택에 아무것도 없는 경우 : 열린 괄호 없이 닫힌 괄호가 들어온 경우
                    return False
                elif c != self.bracket_pairs[stack[-1]]: # 스택에 자신과 짝이 맞지 않는 닫힌 괄호가 들어온 경우
                    return False
                else: # 스택에 자신과 짝이 맞는 닫힌 괄호가 들어온 경우
                    stack.pop()

                # if not stack or c != self.bracket_pairs[stack[-1]]: # 스택에 아무것도 없는 경우 : 열린 괄호 없이 닫힌 괄호가 들어온 경우
                #     return False
                # else:
                #     stack.pop()
        return not stack