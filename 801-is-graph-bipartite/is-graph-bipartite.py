from collections import deque

class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                q = deque([i])
                color[i] = 0

                while q:
                    node = q.popleft()

                    for adj in graph[node]:

                        if color[adj] == -1:
                            color[adj] = 1 - color[node]
                            q.append(adj)

                        elif color[adj] == color[node]:
                            return False

        return True


        