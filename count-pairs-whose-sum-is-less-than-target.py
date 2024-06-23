class Solution:
    def countPairs(self, nums, target: int) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    answer += 1
        return answer


import itertools

class Solution:
    def countPairs(self, nums, target: int) -> int:
        all_combinations = itertools.combinations(nums,2)
        result = 0
        for x,y in all_combinations:
            if x + y < target:
                result += 1
        return result


class Solution:
    def countPairs(self, nums, target: int) -> int:
        return len([x for x,y in itertools.combinations(nums,2) if x+y < target])

# 투포인터 풀이, 직접적인 이분탐색은 아님. 시간복잡도는 while문은 O(n). 정렬은 O(nlogn)
class Solution:
    def countPairs(self, nums, target: int) -> int:
        nums.sort() # sort the vector nums
        count = 0 # variable to store the count
        left = 0 # variable to store the left
        right = len(nums) - 1 # variable to store the right

        while (left < right): # loop until left is less than right
            if (nums[left] + nums[right] < target): # if nums[left] + nums[right] is less than target
                count += right-left # update the count
                left += 1 # increment the left
            else: # else
                right -= 1 # decrement the right
        return count # return the count


class Solution:
    def countPairs(self, nums, target: int) -> int:

        return sum(map(lambda x: x[0]+x[1] < target,
                       itertools.combinations(nums, 2)))
