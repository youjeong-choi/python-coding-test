from statistics import median
from typing import List


class Solution:
    def findNonMinOrMax(self, a: List[int]) -> int:
        return (-1,median(a[:3]))[len(a)>2]


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        else:
            return sorted(nums)[1]


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <3:
            return -1
        else:
            nums.remove(max(nums))
            nums.remove(min(nums))
            return nums[0]