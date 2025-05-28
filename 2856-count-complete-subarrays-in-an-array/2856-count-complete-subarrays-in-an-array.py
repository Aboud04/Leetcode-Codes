class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        dist1 = len(set(nums)) 

        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                if len(seen) == dist1:
                    total += 1
                elif len(seen) > dist1:
                    break  
        return total
