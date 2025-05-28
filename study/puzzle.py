def dfs(i, j, n, k, table, group) :
    if i < 0 or i >= n or j < 0 or j >= n :
        return
    if table[i][j] == k :
        table[i][j] = 1-k
        group.append([i,j])
        dfs(i-1, j, n, k, table, group)
        dfs(i+1, j, n, k, table, group)
        dfs(i, j-1, n, k, table, group)
        dfs(i, j+1, n, k, table, group)


def spin(board) :
    n = len(board) # 행 길이
    m = len(board[0]) # 열 길이
    result = [[0] * n for _ in range(m)] # 90도 회전한 결과는 행과 열이 반대됨
    for i in range(n):
        for j in range(m):
            result[j][n - 1 - i] = board[i][j]
    return result


def solution(game_board, table):
    n = len(table)

    # table 에 있는 블럭 찾기
    blocks = []
    for i in range(n) :
        for j in range(n) :
            if table[i][j] == 1 :
                group = []
                dfs(i, j, n, 1, table, group)
                min_x = min(group, key=lambda x:x[0])[0]
                min_y = min(group, key=lambda x:x[1])[1]

                for k in range(len(group)) :
                    group[k][0] -= min_x
                    group[k][1] -= min_y

                max_x = max(group, key=lambda x:x[0])[0] + 1
                max_y = max(group, key=lambda x:x[1])[1] + 1

                matrix = [[0] * max_y for _ in range(max_x)]

                for x,y in group :
                    matrix[x][y] = 1

                blocks.append(matrix)


    # game_board 에 있는 비어있는 모양 찾기
    empty_board = []
    for i in range(n) :
        for j in range(n) :
            if game_board[i][j] == 0 :
                group = []
                dfs(i, j, n, 0, game_board, group)
                min_x = min(group, key=lambda x:x[0])[0]
                min_y = min(group, key=lambda x:x[1])[1]

                for k in range(len(group)) :
                    group[k][0] -= min_x
                    group[k][1] -= min_y

                max_x = max(group, key=lambda x:x[0])[0] + 1
                max_y = max(group, key=lambda x:x[1])[1] + 1


                matrix = [[0] * max_y for _ in range(max_x)]

                for x,y in group :
                    matrix[x][y] = 1

                empty_board.append(matrix)


    answer = 0
    for i in blocks :
        for shape in empty_board :
            if len(i)*len(i[0]) == len(shape)*len(shape[0]) :
                # print("블럭 : {}, 비어있는 틀 : {}".format(i, shape))
                block = i
                find = False
                for _ in range(4) :
                    if block == shape :
                        # print("블럭 : {}, 비어있는 틀 : {} 이 같음".format(block, shape))
                        for c in block :
                            answer += c.count(1)
                        shape[0][0] = -1 # 이미 블럭을 끼웠으므로 -1 을 넣어 다른 블럭이 오지 못하게 함
                        find = True
                        break
                    else :
                        block = spin(block)
                        # print("회전한 블럭 : {}".format(block))
                if find : break

    return answer