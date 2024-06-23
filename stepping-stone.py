def solution(distance, rocks, n):
    answer = 0

    rocks.append(distance)
    rocks.sort()

    start = 1
    end = distance

    while start <= end:
        mid = (start + end) // 2
        prev = 0
        count = 0

        for rock in rocks:
            if rock - prev < mid:
                count += 1
                if count > n: break
            else:
                prev = rock

        if count > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer