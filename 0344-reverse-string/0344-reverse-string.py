class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(0, int(len(s)/2)):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
 
        """
        Do not return anything, modify s in-place instead.
        """
        