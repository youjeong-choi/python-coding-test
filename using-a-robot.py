from typing import Counter


class Solution:
    def robotWithString(s: str) -> str:
        dic, t, ans = Counter(s), [], []

        for ch in s:
            t.append(ch)
            if dic[ch] == 1:
                del dic[ch]
            else:
                dic[ch] -= 1
            while dic and t and min(dic) >= t[-1]:
                ans += t.pop()
                print(ans)

        ans += t[::-1]
        return ''.join(ans)


class Solution:
    def robotWithString(s: str) -> str:
        cnt, lo, p, t = Counter(s), 'a', [], []
        for ch in s:
            t += ch
            cnt[ch] -= 1

            while lo < 'z' and cnt[lo] == 0:
                lo = chr(ord(lo) + 1)
                print(lo)
            while t and t[-1] <= lo:
                p += t.pop()
                print(p)
        return "".join(p)


class Solution:
    def robotWithString(s: str) -> str:
        ret, n = "", len(s)
        suffixMin = [None]*n

        # construct suffix minimum array
        for i in range(n-1, -1, -1):
            if i == n-1: suffixMin[i] = s[i]
            else: suffixMin[i] = min(s[i], suffixMin[i+1])

        t = []
        for i in range(n):
            # append character at current index i to string t
            t.append(s[i])

            # check whether the last character of string t is not larger than the suffix min at index i+1,
            # if so, it means we cannot find a smaller character from the characters on the right side of current index i,
            # and we should print out the last character of string t
            while t and (i == n-1 or t[-1] <= suffixMin[i+1]): ret += t.pop()
        return ret


print(Solution.robotWithString('xyaxyz'))