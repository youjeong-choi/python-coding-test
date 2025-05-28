# 카드 뭉치, 159994
# 선물로 받은 카드 뭉치 두 개
# 규칙에 따라 카드에 적힌 단어들을 사용해 원하는 순서의 단어 배열(문장)을 만들고 싶음.
# 1 <= len(cards1), len(cards2) <= 10, cards1과 2의 각 원소의 개수도 마찬가지.
# cards1과 2에는 서로 다른 단어만 존재.
# goal의 원소는 cards1과 2의 원소들로만 이루어져 있음.
# 시간 복잡도는 N = len(goal) <= len(cards1) + len(cards2), O(N) 

from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for g in goal:
        if (cards1 and cards1[0] == g):
            cards1.popleft()
        elif (cards2 and cards2[0] == g):
            cards2.popleft()
        else:
            return 'No'
            
    return 'Yes'

solution(["i", "water", "drink"], ["want", "to"],["i", "want", "to", "drink", "water"])