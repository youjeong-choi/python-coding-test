from typing import Counter, List
from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        for i, j in count.items():
            freq[j].append(i)

        for i in range(len(freq) - 1, -1, -1):
            for val in freq[i]:
                ans.append(val)
                if len(ans) == k:
                    return ans

        return []


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find the frequency of each number
        num_frequency_map = {}
        for num in nums:
            num_frequency_map[num] = num_frequency_map.get(num, 0) + 1
        top_k_elements = []

        # go through all numbers of the num_frequency_map
        # and push them in the top_k_elements, which will have
        # top k frequent numbers. If the heap size is more than k,
        # we remove the smallest(top) number
        for num, frequency in num_frequency_map.items():
            heappush(top_k_elements, (frequency, num))
            if len(top_k_elements) > k:
                heappop(top_k_elements)

        # create a list of top k numbers
        top_numbers = []
        while top_k_elements:
            top_numbers.append(heappop(top_k_elements)[1])

        return top_numbers


from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return [x[0] for x in freq.most_common(k)]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [num for num, _ in counter.most_common(k)]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {_:[] for _ in range(len(nums) +1)}
        buckets[0] = set(nums)

        for n in nums:
            for i, b in buckets.items():
                if n in b:
                    b.remove(n)
                    buckets.get(i+1).append(n)
                    break

        ans = []
        for i in range(len(nums), 0, -1):
            if len(ans) < k and len(buckets[i]) > 0:
                ans += buckets[i]

        return ans
