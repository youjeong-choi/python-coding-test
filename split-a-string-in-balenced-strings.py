# Runtime : 56% Memory : 35%
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        for c in s:
            if c == 'R': r += 1
            if c == 'L': l += 1
            if l == r: res += 1
        return res

# Runtime : 12% Memory: 84%
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        s = s.replace("R", "-1,").replace("L", "1,")
        ls = list(map(lambda x : 1 if x == "1" else -1, s[:-1].split(",")))
        c = 0
        k = 0
        for i in ls :
            if k == 0 :
                c += 1
            k += i
        return c


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, ans = 0, 0

        for char in s:
            count += 1 if char == 'R' else -1
            ans += count == 0

        return ans


from itertools import accumulate

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return list(accumulate(1 if c == "R" else -1 for c in s)).count(0)


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = prefix = 0
        for c in s:
            prefix += 1 if c == "R" else -1
            if not prefix: ans += 1
        return ans


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return sum(t == 0 for t in accumulate(
            map({'L':-1,'R':1}.get,s)))