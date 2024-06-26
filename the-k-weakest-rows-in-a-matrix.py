import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hashm=[]
        for i in range(len(mat)):
            hashm.append([mat[i].count(1),i])

        hashm.sort()
        res=[]
        for i in range(k):
            res.append(hashm[i][1])
        return res


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        arr = []
        for i in range(len(mat)):
            heapq.heappush(arr, (sum(mat[i]), i))

        ret = []
        while k > 0:
            node, i = heapq.heappop(arr)
            ret.append(i)
            k -= 1

        return ret


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [x[0] for x in sorted(enumerate(map(sum, mat)), key=lambda x: x[::-1])][:k]

