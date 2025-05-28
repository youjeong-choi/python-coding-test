# 방문 길이, 49994
# 다시 풀어봐야 할 문제

# len(dirs) <= 500
# 처음 걸어본 길
# 경계에서 넘어간 명령은 무시
# only U, D, R, L

def solution(dirs):
    spot = [0, 0]
    road = set()
    # dirs의 한글자씩 좌표로 구별되는 길을 만들어 road에 넣고 그 결과의 개수를 return.
    # 시간복잡도는 O(N), set자료형의 add는 해시를 통해 동작하므로 사실상 O(1)이다. 

    # 이동 방향 정의 (x, y)
    directions = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }

    for dir in dirs:
        dx, dy = directions[dir]
        new_spot = [spot[0] + dx, spot[1] + dy]

        # 좌표 범위 확인 (-5 ~ 5)
        if -5 <= new_spot[0] <= 5 and -5 <= new_spot[1] <= 5:
            if dir == 'U' or dir == 'R':
                # 리스트에 숫자 또는 다른 자료형이 포함되어 있으면, join()을 바로 사용할 수 없습니다.
                # 이때는 map(str, 리스트)를 사용하여 모든 요소를 문자열로 변환한 후 join()을 적용합니다.            
                road.add(','.join(map(str, spot + new_spot)))
            else:
                road.add(','.join(map(str, new_spot + spot)))
            spot = new_spot        

    return len(road)

solution("ULURRDLLU")