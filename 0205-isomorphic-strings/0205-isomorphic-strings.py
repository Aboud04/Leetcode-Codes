class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dicts = {}
        d = {}
        for idx,i in enumerate(s):
            
            if i not in dicts:
                dicts[i] = t[idx]
            else:
                if dicts[i] != t[idx]:
                    return False
            
            if t[idx] not in d:
                d[t[idx]] = i
            else:
                if d[t[idx]] != i:
                    return False
                
        return True
            