class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
            
        s = nums[0]
        e = -1
        ranges = []
        for idx in range(len(nums) - 1):
            if nums[idx] + 1 != nums[idx + 1]:
                e = nums[idx]
                if s == e:
                    ranges.append(str(s))
                else:
                    ranges.append(str(s) + "->" + str(e))
                s = nums[idx + 1]
        e = nums[len(nums) - 1]
        if s == e:
            ranges.append(str(s))
        else:
            ranges.append(str(s) + "->" + str(e))

        return ranges

