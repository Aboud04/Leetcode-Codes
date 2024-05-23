class Solution:
    def isHappy(self, n: int) -> bool:
        
            
        def sumSquare(n):
            total = 0
            while n > 0:
                total += (n%10)**2
                n//=10
            return total
        
        while True:
            n = sumSquare(n)
            if n == 1: return True
            if n == 89: return False
            