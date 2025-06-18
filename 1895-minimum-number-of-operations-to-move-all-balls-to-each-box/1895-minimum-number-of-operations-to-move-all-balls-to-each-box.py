class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        d = dict()
        for idx,v in enumerate(boxes):
            if v == "1":
                d[idx] = idx

        r = []
        for idx,v in enumerate(boxes):
            sm = 0
            for k,_ in d.items():
                if idx != k:
                    sm += abs(k - idx)
            
            r.append(sm)
        
        return r

