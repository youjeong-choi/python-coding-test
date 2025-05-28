# 꼭 각각의 원소가 h-index가 되는 것이 아니다.
# 인덱스 값보다 큰 원소가 인덱스 만큼의 개수로 있는가?
def solution(citations):
    # 일단 오름차순 정렬
    # 맨 처음 원소부터 그 원소의 횟수만큼 그 원소 이상의 값인지 체크
    # 하나씩 늘려가면서 H-index를 늘려나간다.
    answer = 0
    citations.sort()
    for c in range(len(citations)):
        if len(citations) >=  c + citations[c]:
            answer = citations[c]
        else:
            return answer
        # if len(citations[c:c + citations[c]]) == citations[c]:
        #     answer = citations[c]
        # else:
        #     return answer


def solution(citations):
    citations = sorted(citations)
    l = len(citations)

    for i in range(l):
        if citations[i] >= l-i:
            return l-i

    return 0


def solution(citations):
    citations.sort(reverse=True)
    h_index = 0

    for c in citations:
        if c > h_index:
            h_index += 1

    return h_index


def solution(citations):
    sorted_citations = sorted(citations, reverse=True)

    for i in range(len(sorted_citations)):
        if sorted_citations[i] <= i:
            return i

    return len(sorted_citations)

print(solution([0, 1, 3, 5, 6]))