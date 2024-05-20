class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        
        sumAB = int(a, 2) + int(b, 2)
        return str("{0:b}".format(int(sumAB)))
            
            
                         
        