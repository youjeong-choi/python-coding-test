# 기능개발, 42586
# 각 기능은 진도가 100%일 때 배포 가능, 배포는 하루에 한번
# 먼저 개발된 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포가 된다. 가장 앞의 것이 언제 100%가 되는 지가 중요.
# len(progresses) <= 100
# 각 배포마다 몇 개의 기능이 배포되는지 return

import math

def solution(progresses, speeds):
    answer = []
    days = []
    # 각각의 작업에 대해서 며칠이 지나야 진도 100%가 되는지 일수 계산
    for i, p in enumerate(progresses):
        days.append(math.ceil((100 - p) / speeds[i]))

    # 완성 일수 리스트에 대해서 맨 처음 값을 기준점으로 잡기
    release = days[0]
    count = 0
    # 기준점보다 작거나 같은 값에 대해서는 count + 1하고 큰 값이 나오면 기준점을 바꾸고, count 값을 answer에 추가 후 count도 리셋.
    # 시간복잡도는 N = len(progresses), O(N)
    for d in days:
        if d <= release:
            count += 1
        else:
            answer.append(count)
            release = d
            count = 1
    
    # 처리하지 않는 마지막 원소 append 
    answer.append(count)
    return answer

solution([93, 30, 55],[1, 30, 5])