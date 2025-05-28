from typing import List

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        # key point: never use devision to judge whether 3 points are on a same line or not, use the multiplication instead !!

        n = len(stockPrices)
        stockPrices.sort(key = lambda x: (x[0], x[1]))

        if n == 1:
            return 0

        pre_delta_y = stockPrices[0][1] - stockPrices[1][1]
        pre_delta_x = stockPrices[0][0] - stockPrices[1][0]
        num = 1

        for i in range(1, n-1):
            cur_delta_y = stockPrices[i][1] - stockPrices[i+1][1]
            cur_delta_x = stockPrices[i][0] - stockPrices[i+1][0]

            if pre_delta_y * cur_delta_x != pre_delta_x * cur_delta_y:
                num += 1
                pre_delta_x = cur_delta_x
                pre_delta_y = cur_delta_y

        return num


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1:
            return 0

        stockPrices.sort(key = lambda x: x[0])
        ans = 1

        for i in range(1,len(stockPrices)-1):
            if (stockPrices[i+1][1]-stockPrices[i][1])*(stockPrices[i][0]-stockPrices[i-1][0]) != (stockPrices[i+1][0]-stockPrices[i][0])*(stockPrices[i][1]-stockPrices[i-1][1]):
                ans += 1

        return ans


from itertools import pairwise
from fractions import Fraction            # For larger values it will give accurate answer

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        c = None
        k = 0

        for i,j in pairwise(stockPrices):
            x = Fraction(j[1]-i[1],j[0]-i[0])      #(j[1]-i[1]) // (j[0]-i[0])
            if x != c:
                k += 1
                c = x

        return k