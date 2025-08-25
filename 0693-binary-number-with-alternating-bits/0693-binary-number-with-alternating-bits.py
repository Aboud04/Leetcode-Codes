class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        prev = None
        for i in range(int(log(n,2)) + 1):
            if prev != None and prev == (n >> i) & 1:
                return False
            prev = (n >> i) & 1
        return True
