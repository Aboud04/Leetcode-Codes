class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        num1 = 0
        cnt = 0
        mx = 0
        seen = False
        for bit in s:
            if bit == "0":
                if seen:
                    cnt = 0
                    seen = False
                    num1 = 0
                cnt -= 1
                
            
            if bit == "1":
                num1 += 1
                cnt += 1
                seen = True


            if cnt <= 0: mx = max(num1, mx)
            
        
        return mx * 2