class Solution:
    def isHappy(self, n: int) -> bool:
        
        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20,85}
        
        def sumSquare(n):
            total = 0
            while n > 0:
                total += (n%10)**2
                n//=10
            return total
        
        while True:
            n = sumSquare(n)
            if n == 1: return True
            if n in cycle_members: return False
            