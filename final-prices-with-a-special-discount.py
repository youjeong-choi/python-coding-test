from typing import List

# Brute force
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answer = []
        for i in range(n):
            discount = 0
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            answer.append(prices[i] - discount)
        return answer


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    prices[i]-=prices[j]
                    break
        return prices

# Best
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in range(len(prices)):
            while stack and (prices[stack[-1]] >= prices[i]):
                prices[stack.pop()] -= prices[i]
            stack.append(i)
        return prices


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        # right_min Stores the Discount
        right_min = [0] * n
        right_min[-1] = 0 # For the Last Item, there will be No Right Guys, So No Discount i.e 0

        stack = []
        stack.append(prices[-1])
        for i in range(n-2, -1, -1): # Traversing from the End
            # If Stack's Top Guy is Bigger than Current Element,, then Do Pop
            while stack and stack[-1] > prices[i]:
                stack.pop()
            # If Stack's Top Guy is Lesser or Equal to the Current Element, then that Top is Our 1st Right Min.
            if stack and stack[-1] <= prices[i]:
                right_min[i] = stack[-1]
            # If Stack got Empty,, then No Smallest Guy at Right Side
            elif not stack:
                right_min[i] = 0 # prices[i]

            stack.append(prices[i])

        # Subtracting the Right_Min(Discount) Array from the Prices Array
        # Updating Answer is in Discount Array itself
        for i in range(n):
            right_min[i] = prices[i] - right_min[i]

        return right_min