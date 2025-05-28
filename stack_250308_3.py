# 크레인 인형뽑기 게임, 64061
# N * N 크기의 정사각 격자
# 모든 인형은 한 칸을 차지하며 격자의 가장 아래 칸부터 차곡차곡 쌓여 있다.
# 순서대로 집어올린 인형을 바구니에 쌓고, 같은 모양의 인형 두 개가 바구니에 연속해서 쌓일 시 사라진다.
# 인형이 없는 곳에서 크레인 작동 시 아무런 일도 일어나지 않는다.
# 바구니의 제약은 없음.
# board 배열은 5 * 5 이상 30 * 30 이하
# board의 각 칸의 값은 0 이상 100 이하인 정수인데, 0인 경우 빈 칸이다.
# 1 <= len(moves) <= 1000, moves의 각 원소의 값은 1 이상 board 배열의 가로 크기 이하
# 터트려져 사라진 인형의 개수를 return
from collections import deque

def solution(board, moves):
    answer = 0
    n = len(board)
    new = [deque() for i in range(n)]
    bucket = []

    # board의 각 원소를에 대해 1 ~ N 번째 해당하는 인형을 분류하여 새로운 board에 append()
    for b in board:
        for i in range(n):
            if b[i]:
              new[i].append(b[i]) 

    # 그 후에 moves를 순회하며 해당하는 board의 원소를 bucket에 append
    # bucket은 스택으로 마지막 원소와 동일한 원소가 올 시 pop()을 실행하고 answer += 2가 된다.
    for m in moves:
        if new[m -1]:
            # pop(-1)이 아닌 deque로 popleft()를 사용함으로써 시간복잡도를 len(new[m - 1])에서 len(1)로 줄일 수 있다.
            l = new[m - 1].popleft()
            if bucket and bucket[-1] == l:
                bucket.pop()
                answer += 27
            else:
                bucket.append(l)

    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])