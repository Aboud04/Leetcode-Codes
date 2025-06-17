class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        m = -1
        while i + 2 < len(num):
            if num[i] == num[i + 1] == num[i + 2]:
                m = max(m, int(num[i]))
            i += 1
    
        return "" if m == -1 else str(m) * 3