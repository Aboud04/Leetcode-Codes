class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        nums.sort(key=lambda x: x == val)
        for i in nums:
            if i != val:
                k+=1

        return k

    

        