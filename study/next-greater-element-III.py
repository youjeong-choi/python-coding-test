# digit : 십진수로 표현되는 1자리 숫자(0~9)

from typing import List


class Solution:
    def nextPermutation(self, s: list[int]):
        n = len(s)
        for i in range(n - 2, -1, -1):
            a, b = s[i:i+2]

            # 마지막부터 시작해 처음으로 증가가 아닌 포인트 찾기
            if a < b:

                # [i+1, n]d의 범위 안에서 s[i] 보다 큰 값 중에 최소값을 구함
                imin = s.index(min(x for x in s[i+1:n] if x > a), i+1, n)

                # i와 바꾸기
                s[i], s[imin] = s[imin], s[i]

                # [i+1, n] 범위에 대하여 정렬
                s[i+1:n] = sorted(s[i+1:n])

                return s

        return None

    def nextGreaterElement(self, n: int) -> int:
        x = list(str(n))
        x = self.nextPermutation(x)

        if x is None:
            return -1

        x = int(''.join(x))

        if x >= 2 ** 31:
            return -1

        return x


class Solution:

    def nextPermutation(self, num: List[str]):
        """
        returns next permutation of num greater than num.
        Rearranges num in place and returns a True if permutation exists.
        Otherwise returns False
        """

        # i = (pos of first non-increasing digit) + 1
        # 마지막부터 시작해 처음으로 증가가 아닌 포인트 찾기
        i = len(num) - 1
        while i > 0 and num[i-1] >= num[i]:
            i -= 1

        if i == 0:
            return False

        # 바꿀 인덱스 찾기 : 바꿀 값보다 큰 값 중 가장 작은 값에서 멈추기(어차피 나머지는 내림차순 이므로)
        j = i
        while j < len(num) and num[j] > num[i-1]:
            j += 1

        # 바꾸기
        num[i-1], num[j-1] = num[j-1], num[i-1]

        # 4. Arrange digits after partition point in reverse sorted order to get min value.
        num[i:] = reversed(num[i:])
        return True

    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))

        if self.nextPermutation(digits):
            num = int(''.join(digits))

            # Check for 32 bit integer range
            if num <= 2 ** 31:
                return num

        return -1