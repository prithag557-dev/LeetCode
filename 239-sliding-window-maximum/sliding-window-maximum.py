from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        result = []

        for i in range(len(nums)):

            # Remove indices outside the window
            while q and q[0] <= i - k:
                q.popleft()

            # Remove smaller elements
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            # Start adding results once window size is k
            if i >= k - 1:
                result.append(nums[q[0]])

        return result