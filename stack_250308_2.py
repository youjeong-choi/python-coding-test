# 주식가격, 42584
# 2 <= len(prices) <= 100_000
# prices의 각 가격은 1 이상 10_000 이하인 자연수 

def solution(prices):
    # 먼저 answer를 len(prices) = n, n-1인 n개의 원소로 구성
    n = len(prices)
    answer = list(range(n - 1, -1, -1))
    stack = []
    
    # prices의 각 가격을 for문으로 반복하면서 stack에 (가격, 시점)을 append
    # 이전 시점에 비해 떨어진 가격이 나올 시, 하나씩 시점을 뒤로 하며 떨어지지 않은 시점까지 pop() 진행.
    # 떨어지지 않은 시점이 결정되면 answer에 해당하는 인덱스의 위치로 값을 바꾸기.
    for i, price in enumerate(prices):
        while stack and stack[-1][0] > price:
          _, t = stack.pop()
          answer[t] = i - t
        else:
          stack.append((price, i))
        
    return answer

print(solution([1, 2, 3, 2, 3]))