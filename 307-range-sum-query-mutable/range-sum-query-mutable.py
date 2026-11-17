class NumArray:

    def __init__(self, nums):
        self.nums = nums[:]
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)

        def build(node, start, end):
            if start == end:
                self.tree[node] = nums[start]
            else:
                mid = (start + end) // 2
                build(2 * node, start, mid)
                build(2 * node + 1, mid + 1, end)
                self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

        if self.n:
            build(1, 0, self.n - 1)

    def update(self, index, val):
        def change(node, start, end):
            if start == end:
                self.tree[node] = val
            else:
                mid = (start + end) // 2
                if index <= mid:
                    change(2 * node, start, mid)
                else:
                    change(2 * node + 1, mid + 1, end)

                self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

        if self.n:
            change(1, 0, self.n - 1)

    def sumRange(self, left, right):
        def query(node, start, end):
            if left <= start and end <= right:
                return self.tree[node]

            if end < left or start > right:
                return 0

            mid = (start + end) // 2
            return (query(2 * node, start, mid) +
                    query(2 * node + 1, mid + 1, end))

        if not self.n:
            return 0

        return query(1, 0, self.n - 1)