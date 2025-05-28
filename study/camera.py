def solution(routes):
    routes.sort(key = lambda x:x[1])
    cnt = 1
    k = routes[0][1]

    for r in routes:
        if k < r[0]:
            k = r[1]
            cnt += 1
    return cnt


def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0], reverse=True)
    camera = 30001
    for route in routes:
        if camera > route[1]:
            answer += 1
            camera = route[0]
    return answer


solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])