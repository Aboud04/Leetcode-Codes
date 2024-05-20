class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lenA = len(a)
        lenB = len(b)
        numA = 0
        numB = 0
        
        for i in range(lenA):
            numA += int(a[i])* (2**(lenA-1-i))
                                
        for i in range(lenB):
            numB += int(b[i])* (2**(lenB-1-i))
        
        sumAB = numA + numB
        return str("{0:b}".format(int(sumAB)))
            
            
                         
        