class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {0:0}
        for i in nums:
            if i == 0:
                d[0]+=1
        
    
        
        for i in range(d[0]):
            nums.remove(0)
            nums.append(0)
        
                