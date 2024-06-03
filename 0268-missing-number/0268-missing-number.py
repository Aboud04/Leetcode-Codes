class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        length = len(nums)
        total = (length*(length+1))//2
        for i in range(length):
            total-=nums[i]
        return total