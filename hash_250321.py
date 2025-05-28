# 완주하지 못한 선수, 42576
# 단 한 명을 제외하고 모두가 마라톤을 완주
# 1 <= N = len(participant) <= 100_000
# len(completion) = N - 1
# 참가자 중에 동명이인이 있을 수 있음.

import collections

def solution(participant, completion):
    com = {}
    
    for c in completion:
        if c in com: com[c] += 1
        else: com[c] = 1

    for p in participant:
        if p in com:
            if com[p] == 0: return p
            else: com[p] -= 1
        else: return p

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])