class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        columnTitle = columnTitle[::-1]
        val = 0
        for i in range(len(columnTitle)):
            val += (1+(ord(columnTitle[i]) -65)) *(26**i)
            
        return val
            
            
            