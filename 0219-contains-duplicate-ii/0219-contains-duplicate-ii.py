class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) >= len(nums):
            return False
        
        d = {}
        for idx,i in enumerate(nums):
            if i not in d:
                d[i] = idx
            else:
                if abs(d[i]-idx) <= k:
                    return True
                else:
                    del d[i]
                    d[i] = idx
        return False