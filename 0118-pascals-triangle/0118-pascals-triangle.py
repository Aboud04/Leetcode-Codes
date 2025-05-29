class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        l = [[1], [1, 1]]
        for i in range(2, numRows + 1):
            ll = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    ll.extend([1])
                else:
                    ll.extend([l[i-1][j-1] + l[i-1][j]])
            l.extend([ll])
        return [l[0]] + l[2:]

        