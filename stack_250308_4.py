# 표 편집, 81303
# 다시 풀 문제, 결국 나는 시간복잡도가 너무 큼을 알았지만 별다른 방법이 생각나지 않아 리스트로 풀었고 틀렸다.
# 효율성 테스트의 정확한 시간이 나오지 않아도 input의 N이 매우 크면 append와 pop 사용 시 시간복잡도가 많이 드는 리스트는 최대한 피하도록 하자.
# 결론적으로는 삭제된 인덱스만 알면 되므로 실질적으로 리스트를 조작하는 것이 필요하지 않다. 결론을 위해 실질적으로 필요한 과정인지 생각할 것.
# 결국 올바르게 삭제된 인덱스 리스트를 구하면 되는 것이다. 그러면 실질적으로 리스트를 조작하지 않고 k값을 올바르게 조절하면 되는 것이다.
# 이를 위해 실제 리스트는 건드리지 않고 각 원소의 up, down 시의 인덱스만 바꾼다. append, pop과는 달리 임의 접근한 특정 값을 바꾸는 것은 O(1)이기 때문이다.
# 정 생각이 안나면 아래 처럼 풀고 정확성 테스트만이라도 점수를 획득하긴 해야겠다.

# 명령어 기반으로 표의 행을 선택, 삭제, 복구
# "U X", "D X": 현재 선택된 행에서 X칸 위/아래에 있는 행을 선택
# "C": 현재 선택된 행을 삭제한 후, 바로 아래 행 선택, 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택
# "Z": 가장 최근에 삭제된 행을 원래대로 복구. 단 현재 선택된 행은 바뀌지 않는다.
# 처음 표의 행 개수 n, 처음 선택된 행의 위치 k, 수행한 명령어들이 담긴 문자열 배열 cmd
# 명령어 수행 후 처음 표와 비교하여 표의 행의 삭제 여부를 O, X로 표시한 문자열 return
# 5 <= n <= 1_000_000
# 0 <= k < n
# 1 <= len(cmd) <= 200_000

def solution(n, k, cmd):
    # 초기 리스트 만들기
    # 4가지 액션 함수 만들기
    # cmd를 for문을 돌리면서 모든 액션 적용
    # 초기 리스트와 최종 리스트 비교하여 OX 문자열 return
    mutable = list(range(n))
    del_stack = []

    for c in cmd:
        if c.startswith("U"):
            k -= int(c[-1])
        elif c.startswith("D"):
            k += int(c[-1])
        elif c == "C":
            removed = mutable.pop(k)
            del_stack.append(removed)
            if k == len(mutable):
                k -= 1
        else:
            removed = del_stack.pop()
            if mutable[k] > removed:
                k += 1
            mutable.append(removed)
            mutable.sort()
                    
    answer = "".join("X" if i in del_stack else ch for i, ch in enumerate('O' * n))
    return answer

solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"] )