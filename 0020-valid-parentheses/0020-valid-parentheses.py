class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        mapped = {"(": ")", "{": "}", "[": "]"}
        for i in s:

            if i == "(" or i == "{" or i == "[":
                l = [i] + l
            else:
                if len(l) == 0 or mapped[l[0]] != i:
                    return False
                else:
                    l.pop(0)


        
        return len(l) == 0