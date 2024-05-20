class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        hi = len(nums)
        mid = (hi//2) 
        lo = 0
        while lo <= hi:
            if target == nums[mid]: return mid
            elif target > nums[mid]:
                lo = mid
                mid = (mid + hi)//2 
            else: 
                hi = mid
                mid = mid//2 
            if lo == mid or hi == mid:
                if target <= nums[mid]:
                    return mid
                return mid + 1
        
        
        