class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        for i in s:
            if i == '*':
                ans.pop()
            else:
                ans+=[i]
        return "".join(ans)


class Solution:
    def removeStars(self, s: str) -> str:
        res = ""
        to_remove = 0
        # Represents number of symbols we will skip
        # when meet
        for symb in s[::-1]:
            if symb == "*":
                to_remove += 1
                # Skip one more symbol when meet
            else:
                if not to_remove:
                # if to_remove == 0
                    res += symb
                else:
                    to_remove -= 1
                    # Skipping a symbol
        return res[::-1]
        # The recieved string is also reversed, so
        # reverse it to get the answer


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch!="*":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    pass
        ans = ""
        for ch in stack:
            ans+=ch
        return ans