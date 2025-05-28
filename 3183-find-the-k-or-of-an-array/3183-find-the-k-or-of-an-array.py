class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        l = []
        m = max(nums)
        mlen = format(m, 'b')
        for x in nums:
            val = format(x, 'b')
            val = val.zfill(len(mlen))
            l.append(val)
      
        res = [0] * len(mlen)
        for i in l:
            for cnt, j in enumerate(i):
                if j == "1": 
                    res[cnt] += 1
        
        for i, v in enumerate(res):
            if v >= k:
                res[i] = "1"
            else:
                res[i] = "0"
    
        return int("".join(res), 2)
