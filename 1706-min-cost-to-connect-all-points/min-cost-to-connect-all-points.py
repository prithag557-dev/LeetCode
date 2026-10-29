class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)

        dist = [float('inf')] * n
        visited = [False] * n

        dist[0] = 0
        total_cost = 0

        for _ in range(n):
            min_dist = float('inf')
            u = -1

            for i in range(n):
                if not visited[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i

            visited[u] = True
            total_cost += min_dist

            for v in range(n):
                if not visited[v]:
                    cost = (
                        abs(points[u][0] - points[v][0]) +
                        abs(points[u][1] - points[v][1])
                    )

                    if cost < dist[v]:
                        dist[v] = cost

        return total_cost
        