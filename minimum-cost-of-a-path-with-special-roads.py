import heapq
from typing import List


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        filteredRoads = []
        for road in specialRoads:
            a, b, c, d, cost = road
            if cost < abs(a - c) + abs(b - d):
                filteredRoads.append([a, b, c, d, cost])

        dist = {(start[0], start[1]): 0}
        heap = [(0, start[0], start[1])]
        while heap:
            currdist, x, y = heapq.heappop(heap)
            for road in filteredRoads:
                a, b, c, d, cost = road
                if dist.get((c, d), float('inf')) > currdist + abs(x - a) + abs(y - b) + cost:
                    dist[(c, d)] = currdist + abs(x - a) + abs(y - b) + cost
                    heapq.heappush(heap, (dist[(c, d)], c, d))

        res = abs(target[0] - start[0]) + abs(target[1] - start[1])
        for road in filteredRoads:
            a, b, c, d, cost = road
            res = min(res, dist.get((c, d), float('inf')) + abs(target[0] - c) + abs(target[1] - d))

        return res
