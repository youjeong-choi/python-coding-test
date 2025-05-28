from collections import defaultdict, deque

# DFS
class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        l = defaultdict(list)

        for i, j in edges:
            l[i].append(j)
            l[j].append(i)

        s = set()

        def dfs(node):
            if node == destination:
                return True
            s.add(node)

            for j in l[node]:
                if j not in s and dfs(j):
                    return True

            return False

        return dfs(source)


class Solution:
    def dfs(self, node, graph, vis, destination):
        if node == destination:
            return True

        vis[node] = True

        for neighbor in graph[node]:
            if not vis[neighbor]:
                if self.dfs(neighbor, graph, vis, destination):
                    return True

        return False


    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        vis = [False]*n

        return self.dfs(source, graph, vis, destination)

# BFS
class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source])
        visited = set([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False


from typing import List
from collections import deque,defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    # bfs로 풀까
        # visited = set()
        graph = defaultdict(list)

        for u, v in edges:
            # a,b = edge
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source])
        visited = set([source])

        while queue:
            now = queue.popleft()
            if now == destination:
                return True

            for node in graph[now]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)

        return False