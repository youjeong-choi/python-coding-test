def solution(nums, target):
    answer = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] < target:
                answer += 1

    return answer


class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def countPairs(self):
        answer = 0
        n = len(self.nums)
        for i in range(n):
            for j in range(i + 1, n):
                if self.nums[i] + self.nums[j] < self.target:
                    answer += 1
        return answer


from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    answer += 1
        return answer


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        return sum(nums[i] + nums[j] < target
               for i in range(len(nums))
               for j in range(i + 1, len(nums)))