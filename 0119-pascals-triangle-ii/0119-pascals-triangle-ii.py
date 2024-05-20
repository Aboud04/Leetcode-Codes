class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [int(math.factorial(rowIndex) / (math.factorial(j) * math.factorial(rowIndex - j))) for j in range(rowIndex+1)]