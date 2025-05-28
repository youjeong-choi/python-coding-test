# 행렬의 곱셈, 12949
# 내가 진짜 해내고 만다.

def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    # 행렬의 곱셈의 원리에 따라 arr1의 원소를 차례로 꺼낸다.
    # 각 원소에 대해 arr2의 개별 원소의 수만큼 연산을 진행한다.
    # 그 연산은 인덱스로 호출한 arr1과 arr2의 값이다.
    # 핵심은 answer[i][j]에서 i는 arr1[i][?]이고 j는 arr2[?][j]라는 것이다.
    # 시간복잡도는 arr1이 (n * m), arr2가 (m * p)라 했을 때 n * p * 2m, 최대 300만이므로 통과.

    for i, arr in enumerate(arr1):
        for j in range(len(arr2[0])):
          for idx, x in enumerate(arr):
             answer[i][j] += x * arr2[idx][j]
            
    return answer

# 114p의 개선된 코드: 변수를 미리 알기 쉽게 선언해 더 깔끔하게 접근하자.
def solution(arr1, arr2):
  r1, c1 = len(arr1), len(arr1[0])
  r2, c2 = len(arr2), len(arr2[0])
  answer = [[0] * c2 for _ in range(r1)]

  for i in range(r1):
    for j in range(c2):
        for k in range(c1):
          answer[i][j] += arr1[i][k] * arr2[k][j]

  return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))