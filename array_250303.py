# 실패율, 42889
# 다시 풀어봐야 할 문제

def solution(N, stages):
    # N개의 스테이지에 대해 각각 실패율을 구한다.
    # stages를 낮은 스테이지를 도전하는 유저부터 오름차순으로 나타낸다.
    stages.sort()
    failed_ratio = [0] * N
    # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return
    # 시간 복잡도는 O(M * logM + N * logN), M은 stages의 개수
    # 시간 복잡도는 최대 N * M = 1억, 테스트 케이스 1개를 시간 초과로 통과하지 못함.
  
    for i in range(N):
        total = len(stages)
        if (total == 0):
           failed_ratio[i] = 0
           break
        # 여기서 filter를 씀으로써 시간복잡도가 매우 올라갔다. filter가 아닌 while을 썼어야 했다.
        result = list(filter(lambda x : x != i + 1, stages))
        failed_ratio[i] = (total - len(result) ) / total
        stages = result

    answer = [i + 1 for i in sorted(range(len(failed_ratio)), key=lambda i: (-failed_ratio[i], i))]
    return answer


def solution(N, stages):
    # N개의 스테이지에 대해 각각 실패율을 구한다.
    # stages를 낮은 스테이지를 도전하는 유저부터 오름차순으로 나타낸다.
    stages.sort()
    failed_ratio = [0] * N

    # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return
    # 이 경우에는 마지막 스테이지도 따로 계산해야 하며, 모든 스테이지를 클리어한 유저에 대해서도 따로 처리해야하므로 복잡하다.
    n = stages[0]
    count = 0
    for i, stage in enumerate(stages):
        if (stage == n):
            count += 1
            if (i == (len(stages) - 1)):
                failed_ratio[n - 1] = count / (len(stages) - i + count)  
        else:
            failed_ratio[n - 1] = count / (len(stages) - i + count)
            n = stage
            count = 1
                          
    answer = [i + 1 for i in sorted(range(len(failed_ratio)), key=lambda i: (-failed_ratio[i], i))]
    return answer


def solution(N, stages):
    stages.sort()
    failed_ratio = [0] * N  # 각 스테이지의 실패율 저장
    total_players = len(stages)  # 전체 플레이어 수
    index = 0  # stages 배열에서 현재 위치

    for stage in range(1, N + 1):
        if index < len(stages) and stages[index] == stage:
            count = 0  # 현재 스테이지에 머물러 있는 사람 수
            while index < len(stages) and stages[index] == stage:
                count += 1
                index += 1
            failed_ratio[stage - 1] = count / total_players
            total_players -= count  # 다음 스테이지에서 고려할 전체 플레이어 수 감소

    # 실패율을 기준으로 내림차순 정렬, 같다면 작은 번호 우선
    answer = [i + 1 for i in sorted(range(N), key=lambda i: (-failed_ratio[i], i))]
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))