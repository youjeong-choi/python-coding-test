# BFS 풀이
# 시간복잡도 : O(n * 2^n)
def solution(numbers, target):
    answer = 0
    leaves = [0]

    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp

    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer


#########################################################
# DFS 풀이
# 시간복잡도 : O(2^n)
def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer

def DFS(numbers, target, depth):
    answer = 0

    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else: return 0

    else:
        answer += DFS(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        return answer


#########################################################
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


#########################################################
from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


#########################################################
def dfs(numbers, target, idx, values): # idx : 깊이 / values : 더하고 뺄 특정 leaf 값
    global cnt
    cnt = 0

    # 깊이가 끝까지 닿았으면
    if idx == len(numbers) & values == target:
        cnt += 1
        return

    # 끝까지 탐색했는데 sum이 target과 다르다면 그냥 넘어간다
    elif idx == len(numbers):
        return

    # 재귀함수로 구현
    dfs(numbers, target, idx+1, values + numbers[idx]) # 새로운 value 값 세팅
    dfs(numbers, target, idx+1, values - numbers[idx])

def solution(numbers, target):
    global cnt
    dfs(numbers, target, 0, 0)
    return cnt