# set을 활용하여 중복 제거
def solution(nums):
    set_nums = len((set(nums))) # set으로 변환시켜 중복 제거 후 원소의 개수
    k = len(nums) // 2 # 선택해야하는 개수

    return min(set_nums, k)

    # if k <= set_nums:
    #     return k
    # else:
    #     return set_nums

# for문을 돌려서 중복 제거
def solution(nums):
    num = {}
    for i in nums:
        if i not in num:
            num[i] = True
    return min(len(nums)/2, len(num))

print(solution([3,1,2,3]))