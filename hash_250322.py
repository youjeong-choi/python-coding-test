# 할인 행사, 131127
# 마트는 일정 금액 지불 시 10일 동안 회원 자격 부여
# 회원을 대상으로 매일 한 가지 제품을 할인하는 행사, 하루에 하나씩만 구매 가능
# 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우 회원가입
# 1 <= len(want) = len(number) <= 10
# number의 원소의 합은 10
# 10 <= len(discount) <= 100_000
# want와 discount의 원소들은 알파벳 소문자로 이뤄진 1 이상 12 이하의 길이 문자열
# 회원등록 날짜의 총 일수 return
from collections import Counter

def solution(want, number, discount):
    answer = 0
    # want로 counter 객체 만들기
    # 하나씩 for문을 돌면서 Counter 객체를 채워넣을 수도 있고, zip()을 한 뒤 바로 dict()을 하여 딕셔너리로 바꾸어 Counter()로 처리할 수 있다.
    want_counter = Counter(dict(zip(want, number))) 

    # discount의 0부터 len(discount) - 10까지를 기점으로 각각 10개를 counter 객체로 만들어서 비교하기
    # 시간 복잡도는 N = len(discount), O(N)
    for i in range(len(discount) - 9):
        discount_counter = Counter(discount[i: i + 10])
        if want_counter == discount_counter: answer += 1

    return answer

solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])