class Solution:
    def relativeSortArray(self, arr1, arr2):
        freq = [0] * 1001

        # Count frequency of elements in arr1
        for num in arr1:
            freq[num] += 1

        result = []

        # Add elements according to arr2 order
        for num in arr2:
            while freq[num] > 0:
                result.append(num)
                freq[num] -= 1

        # Add remaining elements in ascending order
        for num in range(1001):
            while freq[num] > 0:
                result.append(num)
                freq[num] -= 1

        return result