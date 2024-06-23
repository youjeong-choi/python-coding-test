from collections import defaultdict

def solution(n, results):
    rank_array = [[0]*n for _ in range(n)]

    for win, lose in results:
        rank_array[win-1][lose-1] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if rank_array[i][j] == 0 and rank_array[i][k] and rank_array[k][j]:
                    rank_array[i][j] = 1

    column_sum = [0] * n
    row_sum = [0] * n

    for row in range(n):
        for column in range(n):
            column_sum[column] += rank_array[row][column]
            row_sum[row] += rank_array[row][column]

    answer = 0

    for index in range(n):
        if column_sum[index] + row_sum[index] == n - 1:
            answer+=1

    return answer


def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)

    for result in results:
            lose[result[1]].add(result[0])
            win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1

    return answer


def solution(n, results):
    answer = 0
    rank = {i + 1: [set(), set()] for i in range(n)}

    for win, lose in results:
        rank[win][0].add(lose)
        rank[lose][1].add(win)

    for _ in range(2):
        for i in rank.keys():
            for wins in rank[i][0]:
                rank[i][0] = rank[i][0].union(rank[wins][0])

            for loses in rank[i][1]:
                rank[i][1] = rank[i][1].union(rank[loses][1])

    for i in rank.keys():
        if len(rank[i][0]) + len(rank[i][1]) == n - 1:
            answer += 1

    return answer