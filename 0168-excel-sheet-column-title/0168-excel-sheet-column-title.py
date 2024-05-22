class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        div = (columnNumber - 1) // 26
        result = ""
        while columnNumber > 0:
            columnNumber -=1
            result += chr(columnNumber % 26 + (65))
            columnNumber //=26
            
        
        return result[::-1]