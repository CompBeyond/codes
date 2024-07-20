class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(10):
            if i in nums1 and i in nums2:
                return i
        d_1 = min(nums1)
        d_2 = min(nums2)
        return min(d_1, d_2) * 10 + max(d_1, d_2)
