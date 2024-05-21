class Solution:
    def findMaxK(self, nums: List[int]) -> int:
      
        d = {}
        curr = -1
        maxs = -1
        for i in  set(nums):
            d[(abs(i))] = d.get(abs(i), 0) + 1
        
        for key,val in d.items():
            if val == 2:
                curr = key
            if maxs < curr:
                maxs = curr
            
        return maxs