class Solution:
    def climbStairs(self, n: int) -> int:
        ratio =  (1+(5**0.5))/2
        return int(((ratio**(n+1)) - (1-ratio)**(n+1))/(5**0.5))
        