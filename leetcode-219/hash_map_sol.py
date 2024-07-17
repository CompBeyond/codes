class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}
        n = len(nums)
        for i in range(n):
            elem = nums[i]
            last_seen_pos = hmap.get(elem)
            if last_seen_pos != None and i - last_seen_pos <= k:
                return True
            hmap[elem] = i
        return False
