from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Convert all numbers to strings
        nums = list(map(str, nums))

        # Custom comparison
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        # Sort using custom comparison
        nums.sort(key=cmp_to_key(compare))

        # If the largest number is 0, return "0"
        if nums[0] == "0":
            return "0"

        # Join all numbers
        return "".join(nums)