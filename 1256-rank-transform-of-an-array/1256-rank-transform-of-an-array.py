class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sarr = sorted(arr)
        d = dict()
        count = 1
        for i in sarr:
            if i not in d:
                d[i] = count
                count += 1

        for i in range(len(arr)):
            arr[i] = d[arr[i]]

        return arr