class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle not in haystack:
            return -1
        
        string = ""
        for i in range(0,len(haystack)):
            string = haystack[i:i+len(needle)]
            if string == needle:
                return i
        