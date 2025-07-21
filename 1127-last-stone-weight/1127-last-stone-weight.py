class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        scopy = [x for x in stones]
        for i,v in enumerate(stones):
            if len(scopy) == 1:
                return scopy[0]
            if len(scopy) == 0:
                return 0
            m1 = max(scopy)
            scopy.remove(m1)
            m2 = max(scopy)
            diff = m1 - m2
            scopy.remove(m2)
            if diff != 0:
                scopy.append(diff)
            
