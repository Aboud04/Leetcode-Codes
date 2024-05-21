class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = list(set(nums))
        for i,val in enumerate(nums):
            nums[i] = abs(val)
      
        nums = sorted(nums)
        nums = nums[::-1]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
            
        return -1