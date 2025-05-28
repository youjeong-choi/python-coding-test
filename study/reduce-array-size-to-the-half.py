from typing import Counter, List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        selected = set()

        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        removed_count = 0

        for num, freq in sorted_counts:
            selected.add(num)

            removed_count += freq
            if removed_count >= len(arr) // 2:
                break

        return len(selected)


from heapq import heapify, heappop, heappush

class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        # count the amount of occurences
        cn = Counter(arr)

        # heapify the counter (minus for maxheap)
        cn = [-value for value in cn.values()]
        heapify(cn)

        # get the amount of numbers we need to forget
        amount = len(arr)//2 + len(arr) % 2
        counter = 0
        while amount > 0:
            amount += heappop(cn)
            counter += 1

        return counter


def minSetSize(arr):
    count = Counter(arr)
    currentCount = 0
    currentSize = 0

    for value in sorted(count.values(), key=None, reverse=True):
        currentSize += 1
        if currentCount + value >= len(arr) // 2:
            return currentSize
        currentCount += value


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        N = len(arr)
        n = 0
        ans = 0
        for k, val in sorted(c.items(), key = lambda x: -x[1]):
            n += val
            ans += 1
            if n >= (N//2):
                break
        return ans


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        counter, half, length = 0, len(arr) // 2, len(arr)

        for x in sorted(Counter(arr).values(),reverse=True):
            length -= x
            counter += 1
            if length <= half:
                return counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        heap = []
        dic = Counter(arr)
        for i, j in dic.items():
            heappush(heap, [-j, i])

        n = len(arr)
        j = len(arr)
        c = 0
        while n > j//2:
            a = heappop(heap)
            n -= abs(a[0])
            c += 1
            if n <= j//2:
                break
            else:
                b = heappop(heap)
                n -= abs(b[0])
                c += 1
                if n < j//2:
                    break

        return c


def minSetSize(self, arr: List[int]) -> int:
	count = Counter(arr)
	count = sorted([count[i] for i in count])
	n = len(arr)
	temp = 0
	ans = 0

	while(temp < n//2):
		temp += count.pop()
		ans += 1
	return ans