# WORST 1: 일일히 비교, 시간 초과
def solution(phone_book):
    # 접두어의 가장 앞글자와 일치하는 것이 있는지 확인
    # 리스트를 오름차순으로 정렬
    # 맨 처음 원소부터 비교를 시작
    # 원소의 글자 수 만큼 모든 원소들을(자신과 그 이후에 나온 원소들) 자른 뒤 비교
    # But, 시간 초과
    # 아래의 경우 sort()를 사용하였으면 굳이 모든 걸 탐색할 필요 X, 해당하는 원소의 다음 원소만 탐색 O
    phone_book.sort()

    for idx in range(len(phone_book)):
        copy = phone_book[idx:]
        k = len(copy[0])

        for index, val in enumerate(copy):
            if index == 0:
                continue
            if copy[0] == val[0:k]:
                return False

        # if len(set(copy)) != len(pb[idx:]):
        #     return False

    return True

# WORST 2: 일일히 비교, 역시 시간 초과
def solution(phone_book):
    for i in range(len(phone_book)):
        phone_number = phone_book[i]

        for j in range(i+1, len(phone_book)):
            k = min(len(phone_number), len(phone_book[j]))

            if phone_number[:k] == phone_book[j][:k]:
                return False

    return True

# 자료에 대한 조회가 빈번 => 해시를 이용, 여기서는 딕셔너리
# BEST: 해시를 이용
def solution(phone_book):
    hash_map = {}

    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False

    return True

# sort를 사용하여 시간복잡도를 낮출 수 있다.
def solution(phone_book):
    phone_book.sort()

    for phone_number1, phone_number2 in zip(phone_book, phone_book[1:]):
        if phone_number2.startswith(phone_number1):
            return False

    return True


def solution(phone_book):
    phone_book.sort()

    for index, phone_number in enumerate(phone_book):
        if index + 1 != len(phone_book) and phone_book[index + 1].startswith(phone_number):
            return False

        # if index + 1 == len(phone_book):
        #     continue
        # if phone_number == phone_book[index + 1][0:len(phone_number)]:
        #     return False

    return True

print(solution(["119", "97674223", "1195524421"]))