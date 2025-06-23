class Solution:
    def reverse(self, x: int) -> int:
        signed = -1 if x < 0 else 1
        v = str(x)[1:] if signed == -1 else str(x)
        if len(v) < 10: return  int(v[::-1]) * signed

        const1 = "2147483648"
        const2 = "2147483647"
        for i in range(len(v)):
            if signed == -1: 
                if v[len(v) - 1 - i] < const1[i]: return int(v[::-1]) * signed
                elif v[len(v) - 1 - i] > const1[i]: return 0
            else: 
                if v[len(v) - 1 - i] < const2[i]: return int(v[::-1]) * signed
                elif v[len(v) - 1 - i] > const2[i]: return 0
        return 0