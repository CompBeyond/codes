class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        nums_dict = {nums[i]: i for i in range(n)} # O(n)
        for i in range(n): # O(n)
            search = target - nums[i]
            pos = nums_dict.get(search)
            if pos and pos != i:
                return [i, pos]
        #Overall complexity O(2n) = O(n)
