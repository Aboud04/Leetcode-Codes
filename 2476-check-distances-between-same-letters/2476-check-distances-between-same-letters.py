class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = dict()
        for idx, v in enumerate(s):
            if v not in d:
                d[v] = idx
            else:
                d[v] = idx - d[v] - 1  
        
        for k, v in d.items():
            r = ord(k) - 97
            if v != distance[r]:  
                return False
        
        return True