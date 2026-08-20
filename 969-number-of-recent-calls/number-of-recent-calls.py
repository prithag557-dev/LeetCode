from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)

        # Remove requests outside [t - 3000, t]
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)