class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        arr = []
        if len(nums) == 0:
            return [[lower,upper]]
        
        if len(nums) == 1:
                if nums[0] > lower:
                    arr.append([lower,nums[0]-1])
                if nums[0] < upper:
                    arr.append([nums[0]+1,upper])
       
        for i in range(len(nums)):
            if i != len(nums) -1:
                if i == 0 and nums[i] > lower:
                    arr.append([lower,nums[i]-1])
                if nums[i+1] - nums[i] >1:
                    arr.append([nums[i]+1,nums[i+1]-1])
                if i + 1 == len(nums) -1 and nums[i +1] < upper:
                    arr.append([nums[i+1]+1,upper])
        
        return arr