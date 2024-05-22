class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        val = 0
        for i in range(len(columnTitle)-1,-1,-1):
            print(columnTitle[i])
            val += (1+(ord(columnTitle[i]) -65)) *(26**(len(columnTitle)-1-i))
            
        return val
            
            