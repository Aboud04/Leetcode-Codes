class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = []
        for i in range(len(nums)):
            n.append(nums[nums[i]])
        return n
