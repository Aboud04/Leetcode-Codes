class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n + 1):
            lst.append(format(i, 'b').count("1"))
        
        return lst