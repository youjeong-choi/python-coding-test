# 두 개 뽑아서 더하기, 68644

from itertools import combinations

def solution(numbers):
    answer = []
    length = len(numbers)
    for i in range(length):
        for l in range(i + 1, length):
            answer.append(numbers[i] + numbers[l])
    
    answer = sorted(list(set(answer)))     
    return answer

# sorted() 함수는 항상 리스트(list)를 반환
# 입력이 set, tuple, dict_keys 등이어도 결과는 list
def solution(numbers):
    return sorted(set(sum(i) for i in list(combinations(numbers, 2))))


def solution(numbers):
    answer = set()  # 중복 제거를 위해 set 사용
    for a, b in combinations(numbers, 2):
        answer.add(a + b)  # O(1) 삽입

    return sorted(answer)  # O(M log M), M ≤ N², 시간복잡도는 O(M log M) (정렬) ≈ O(N²) (최악의 경우 M ≈ N²이므로)

print(solution([2,1,3,4,1]))