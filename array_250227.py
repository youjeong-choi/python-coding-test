# 모의고사, 42840
# n <= 10_000
# 1번: 1 2 3 4 5 / 1 2 3 4 5 ... = 5의 배수 단위
# 2번: 2 1 2 3 2 4 2 5 / 2 1 2 3 2 4 2 5 ... = 8의 배수 단위 
# 3번: 3 3 1 1 2 2 4 4 5 5 / 3 3 1 1 2 2 4 4 5 5 ... = 10의 배수 단위

# 각각의 문제를 대조하여 채점을 해야 한다.
# 시간 복잡도는 O(n)

def solution(answers):
    score = { 1:0, 2:0, 3:0 }
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    len_1 = len(first)
    len_2 = len(second)
    len_3 = len(third)
    
    # answers에 대해 일일히 for문을 통해 채점하기
    for i, ans in enumerate(answers):     
    # answers의 인덱스를 통해 배수 단위로 반복되는 각 번호의 답을 구한다.
    # 예시) 1번의 경우 i+1의 값을 5로 나눈 나머지가 1이면 0, 2면 1, 0이면 -1 즉 (나머지-1)값으로 인덱스에 접근한다.
    # 정답이 맞는 경우에만 score의 각 번호의 숫자를 늘린다.
        if first[((i + 1) % len_1) - 1] == ans: score[1] += 1
        if second[((i + 1) % len_2) - 1] == ans: score[2] += 1
        if third[((i + 1) % len_3) - 1] == ans: score[3] += 1

    # 최종 score를 (i, score) 형태로 answer에 추가한 뒤에 이를 정렬하여 가장 score가 높은 번호 순으로 리턴
    total_score = list(score.items())
    total_score.sort(key = lambda x : (-x[1], x[0]))
    top = total_score[0][1]
    answer = [x[0] for x in total_score if x[1] == top]
    # total_score_2 = (list(map(lambda x : x[0], total_score)))
    # print(total_score_2)
    return answer


# 개선 코드
def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    len_1, len_2, len_3 = len(first), len(second), len(third)  # 길이 미리 저장
    scores = [0, 0, 0]  # 각 수포자의 점수 저장, 어차피 인덱스값으로 누구의 점수인지 알 수 있으므로 딕셔너리를 쓰지 않아도 된다.

    for i, ans in enumerate(answers):
        if first[i % len_1] == ans: scores[0] += 1
        if second[i % len_2] == ans: scores[1] += 1
        if third[i % len_3] == ans: scores[2] += 1

    max_score = max(scores) # 최대값만 알고 있으면 그 값을 가진 것만 걸러낼 수 있다. 그 값을 가진 번호는 (인덱스 + 1)로 알아낸다.
    return [i + 1 for i, score in enumerate(scores) if score == max_score]

print(solution([1,2,3,4,5]))