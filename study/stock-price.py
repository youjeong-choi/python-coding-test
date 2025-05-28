def solution(prices):
    n = len(prices)
    answer = [0] * n # 가격이 떨어지지 않은 기간을 저장할 배열
    stack = [0] # 스택을 사용해 이전 가격과 현재 가격을 비교, 스택 초기화

    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]: # 가격이 떨어졌으므로 이전 가격의 기간 계산
            j = stack.pop()
            answer[j] = i - j

        stack.append(i)

    # 스택에 남아 있는 인덱스들은 가격이 끝까지 떨어지지 않은 경우의 가격의 인덱스
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer