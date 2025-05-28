# 괄호 회전하기, 76502
# 올바른 괄호 문자열: (), [], {} + 중첩된 경우 + 병렬된 경우
# 0 <= x < len(s)
# s를 왼쪽으로 x칸만큼 회전 시, 올바른 괄호 문자열이 되는 x의 개수 return
# 1 <= len(s) <= 1000

def solution(s):
    answer = 0
    cycle = [s]
    pair = {'[':']', '(':')', '{':'}'}

    # s를 x칸만큼 회전시키는 문자열 리스트 만들기, 시간복잡도는 n = len(s), O(n^2)
    # or 반복되는 컨셉이므로 나누기를 통한 나머지로 인덱스 접근 가능.
    for v in range(len(s)-1):
        cycle.append(cycle[-1][1:] + s[v])
    
    # 리스트에 있는 각 문자열에 대해 올바른 괄호 문자열인지 일일히 확인하여 맞으면 answer의 값을 +1하기
    # 시간 복잡도는 O(n^2), n은 최대 1000이므로 통과
    for x in cycle:
        stack = []
        for y in x:
            if y in pair: # 열린 괄호
              stack.append(y)
            else: # 닫힌 괄호
                if len(stack) == 0: # 열린 괄호가 먼저 나오기 전에 닫힌 괄호가 나온다면 불가능
                    stack.append(y)
                    break
                else:
                  if (pair[stack[-1]] == y): # 열린 괄호와 함께 상쇄
                    stack.pop()
                  else: # 열린 괄호와 함께 상쇄되지 못한다면 불가능
                    stack.append(y)
                    break
                
        if not stack:
            answer += 1

    return answer

solution("}}}")