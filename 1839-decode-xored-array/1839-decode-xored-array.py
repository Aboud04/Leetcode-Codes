class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        arr = [first]
        for i in range(len(encoded)):
            arr.append(encoded[i] ^ first)
            first = arr[i + 1]

        return arr