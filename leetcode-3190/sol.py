class Solution(object):
    def minimumOperations(self, nums):
        result = 0
        for num in nums:
            result += (1 if num % 3 != 0 else 0)
        return result
