class Solution:
    def sortArray(self, nums):
        # Range of possible values
        offset = 50000
        size = 100001

        # Count occurrences
        count = [0] * size

        for num in nums:
            count[num + offset] += 1

        # Put values back into nums in sorted order
        index = 0

        for i in range(size):
            while count[i] > 0:
                nums[index] = i - offset
                index += 1
                count[i] -= 1

        return nums
        