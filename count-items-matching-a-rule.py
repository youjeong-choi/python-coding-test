from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if(ruleKey == 'type'):
            k = 0
        elif(ruleKey == 'color'):
            k = 1
        else:
            k = 2

        answer = 0
        for i in items:
            if(i[k] == ruleValue):
                answer += 1

        return answer


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {'type': 0, 'color': 1, 'name': 2}
        return sum(1 for item in items if item[d[ruleKey]] == ruleValue)


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {'type': 0, 'color': 1, 'name': 2}
        return sum(1 if item[d[ruleKey]] == ruleValue else 0 for item in items)