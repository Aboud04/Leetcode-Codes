class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
       

        Pascal = []

        for i in range(numRows):
            row = []
            for j in range(i + 1):
                row.append(int(math.factorial(i) / (math.factorial(j) * math.factorial(i - j))))
            Pascal.append(row)

        return Pascal


        