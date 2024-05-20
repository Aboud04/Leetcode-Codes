class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip().split(" ")
        
        return len(s[-1])