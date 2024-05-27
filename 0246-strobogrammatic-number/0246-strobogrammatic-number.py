class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        d={'0':'0','1':'1',
            '6':'9','8':'8','9':'6'}
        
        for i in range(math.ceil(len(num)/2)):
            if not(num[i] in d and d[num[i]]==num[-i-1]):
                return False
        return True
        