class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        count = 0

        def dfs(city):
            visited[city] = True

            for i in range(n):
                if isConnected[city][i] == 1 and not visited[i]:
                    dfs(i)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count
        